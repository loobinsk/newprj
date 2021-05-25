from django.template.loader import get_template
from django.template.loader_tags import BlockNode, ExtendsNode
from django.template import Context
from django.conf import settings
from django.core import mail
from mail_templated.template import render_block_to_string
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site


class EmailMessage(mail.EmailMultiAlternatives):
    """Extends standard EmailMessage class with ability to use templates"""

    def __init__(self, template_name, context, *args, **kwargs):
        self.template_name = template_name
        self.context = context
        headers = kwargs.get('headers', {})
        if context.get('unsubscribe_code', None):
            headers['List-Unsubscribe'] = '<http://%s%s?code=%s>' % (Site.objects.get_current().domain, reverse('subscribe:unsubscribe'), context.get('unsubscribe_code', None))
            headers['Precedence'] = 'bulk'

        super(mail.EmailMultiAlternatives, self).__init__(headers=headers, *args, **kwargs)
        self.alternatives = []
        self.subject = context.get('subject', None)

    def get_template_blocks(self, template):
        result = {}
        for node in template.nodelist.get_nodes_by_type(BlockNode):
            result[node.name] = node
        for node in template.nodelist.get_nodes_by_type(ExtendsNode):
            context = Context()
            context.template = template
            result.update(self.get_template_blocks(node.get_parent(context)))
        return result


    def send(self, *args, **kwargs):
        context = Context(self.context)
        tpl = get_template(self.template_name)
        blocks = self.get_template_blocks(tpl.template)
        render_text = tpl.render(context)
        if 'html' in blocks:
            self.attach_alternative(render_text, 'text/html')
        else:
            self.body = render_text
        return super(mail.EmailMultiAlternatives, self).send(*args, **kwargs)


def send_mail(template_name, context, from_email=None, recipient_list=None,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, user=None, subscribe_code=None,  *args, **kwargs):
    """
    Easy wrapper for sending a single message to a recipient list using
    django template system.
    All members of the recipient list will see the other recipients in
    the 'To' field.

    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.
    """

    connection = connection or mail.get_connection(username=auth_user,
                                    password=auth_password,
                                    fail_silently=fail_silently)
    if user and subscribe_code:
        from main.models import Subscribe
        context.update({
            'unsubscribe_code': Subscribe.get_unsubscribe_code(subscribe_code, user)
        })
    return EmailMessage(
        template_name, context, None, None, from_email, recipient_list,
        connection=connection, *args, **kwargs).send()


def send_mail_admins(template_name, context, from_email=None,
                     fail_silently=False, auth_user=None, auth_password=None,
                     connection=None, *args, **kwargs):
    return send_mail(template_name, context, from_email, [admin[1] for admin in settings.ADMINS],
                     fail_silently, auth_user, auth_password,
                     connection, *args, **kwargs)
