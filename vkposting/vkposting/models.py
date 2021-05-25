# coding=utf8
from django.db import models
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import vk_api
from django.template import loader, Context
from django.utils import timezone


class Profile(models.Model):
    login = models.CharField('Логин', max_length=50, default='', blank=True, null=True)
    password = models.CharField('Пароль', max_length=50, default='', blank=True, null=True)
    consumer_key = models.CharField(max_length=100, default='', blank=True, null=True)
    consumer_secret = models.CharField(max_length=100, default='', blank=True, null=True)
    access_token = models.CharField(max_length=100, default='', blank=True, null=True)
    access_token_secret = models.CharField(max_length=100, default='', blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.login if self.login else self.consumer_key


class Canal(models.Model):

    TYPE_VK = 'vk'
    TYPE_TWITTER = 'twitter'
    TYPES = {
        TYPE_VK: 'Вконтакте',
        TYPE_TWITTER: 'Twitter',
    }

    type = models.CharField('Тип', max_length=10, default=TYPE_VK, choices=TYPES.items())
    profile = models.ForeignKey(Profile, verbose_name='Профиль', default=None)
    title = models.CharField('Название', max_length=50, default='')
    code = models.CharField('Символьный код', max_length=50, default='')
    group_id = models.CharField('Код группы ВК', max_length=20, default='')

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'

    def __str__(self):
        return self.title

    def post(self, context, images=[], template=None, content_object=None):
        if self.type == self.TYPE_VK:
            return self.post_vk(context, images, template, content_object)
        elif self.type == self.TYPE_TWITTER:
            return self.post_twitter(context, images, template, content_object)

    def post_vk(self, context, images=[], template=None, content_object=None):
        session = vk_api.VkApi(self.profile.login, self.profile.password)
        session.auth()
        vk = session.get_api()
        if template:
            tpl = loader.get_template(template)
        else:
            tpl = loader.get_template('vkposting/default.txt')
        message = tpl.render(Context(context))

        attach_ids = []
        if images:
            upload = vk_api.VkUpload(session)
            for image in images:
                try:
                    photo = upload.photo_wall(image, group_id=self.group_id)
                    if photo:
                        attach_ids.append('photo%s_%s' % (photo[0]['owner_id'], photo[0]['id']))
                except:
                    pass
        response = vk.wall.post(owner_id='-'+self.group_id,
                         message=message,
                         from_group=1,
                         attachments=','.join(attach_ids)+',')

        if 'post_id' in response:
            if content_object:
                post = Post(canal=self, content=content_object)
                post.save()
            return True
        else:
            return False

    def post_twitter(self, context, images=[], template=None, content_object=None):
        import tweepy

        # auth = tweepy.OAuthHandler(self.profile.consumer_key, self.profile.consumer_secret)
        # auth.set_access_token(self.profile.access_token, self.profile.access_token_secret)
        # api = tweepy.API(auth)

        # if template:
        #     tpl = loader.get_template(template)
        # else:
        #     tpl = loader.get_template('vkposting/twitter.txt')
        # message = tpl.render(Context(context))

        # if images:
        #     api.update_with_media(images[0], message)
        # else:
        #     api.update_status(message)

        # if content_object:
        #     post = Post(canal=self, content=content_object)
        #     post.save()
        return True

    def exists(self, content_object):
        return Post.objects.filter(content=content_object, canal=self).count() > 0


class Post(models.Model):
    canal = models.ForeignKey(Canal)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'object_id')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
