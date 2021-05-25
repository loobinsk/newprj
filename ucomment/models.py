#-*- coding: utf-8 -*-

from django.db import models
from uprofile.models import User
import mptt
from datetime import datetime
import os
import random
import string
import urllib2
from django.core.files.base import ContentFile


def get_comment_image_path(instance, filename):
    fname, ext = os.path.splitext(filename)
    return os.path.join('comment', str(instance.id),
                        ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10)) + ext)


class Comment(models.Model):
    """
    Комментарии
    """
    user = models.ForeignKey(User, verbose_name=u'Пользователь', null=True, blank=True)
    name = models.CharField('Ваше имя', max_length=250, null=True, blank=True)
    image = models.ImageField(u'Фото', upload_to=get_comment_image_path, null=True, blank=True)
    vkid = models.CharField('VK ID', max_length=20, null=True, blank=True)
    text = models.TextField(u'Текст', max_length=500, null=True, blank=True, default='')
    date = models.DateTimeField(u'Дата', default=datetime.now())
    parent = models.ForeignKey('self', verbose_name=u'Комментарий', null=True, blank=True)
    key = models.CharField(u'Ключ ветки', max_length=50, db_index=True)
    url = models.URLField(u'Ссылка', max_length=250, default='', null=True, blank=True)

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'

    def __unicode__(self):
        return self.text

    def load_image(self, href):
        try:
            img = urllib2.urlopen(href)
            f = ContentFile(img.read())
            self.image.save(get_comment_image_path(self, href.split('?')[0]), f, save=True)
            return True
        except:
            return False



mptt.register(Comment, )


def load_from_vk():
    import requests, json
    offset = 0
    while True:
        r = requests.get('https://api.vk.com/method/widgets.getComments?widget_api_id=%s&url=%s&count=%s&offset=%s' % ('2840375', 'http://bazavashdom.ru/otzhiv', 200, offset))
        data = json.loads(r.text)
        exists = False
        for element in data['response']['posts']:
            exists = True

            # получаю информацию о пользователе для определения города
            ruser = requests.get('https://api.vk.com/method/users.get?user_ids=%s&fields=photo_100' % element['from_id'])
            user_data = json.loads(ruser.text)
            user = user_data['response'][0]

            comment = Comment(name=user['first_name'],
                              text=element['text'].replace(u'<br>', u'\r\n'),
                              date=datetime.fromtimestamp(element['date']),
                              key='vashdom',
                              vkid=element['from_id'])
            comment.save()
            comment.load_image(user['photo_100'])

        offset += 200
        if not exists:
            break



