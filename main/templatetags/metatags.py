from django import template
from django.contrib.sites.shortcuts import get_current_site

from main.models import Metatag


register = template.Library()


class MetadataNode(template.Node):
    def __init__(self, variable_name):
        self.variable_name = variable_name

    def render(self, context):
        request = context['request']
        site = get_current_site(request)
        
        metatags = Metatag.objects.filter(site=site, path=request.path)

        if metatags and self.variable_name is not None:
            context[self.variable_name] = metatags[0]
        return ''

@register.tag
def get_metatag(parser, token):
    bits = list(token.split_contents())
    tag_name = bits[0]
    variable_name = bits[2]

    return MetadataNode(variable_name = variable_name)