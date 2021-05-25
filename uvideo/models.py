# coding=utf8
from django.db import models
import random
import os
import string
from datetime import datetime
from uprofile.models import User


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def get_user_video_thumb_path(instance, filename):
    fname, ext = os.path.splitext(filename)
    return os.path.join('user', str(instance.user.id), 'video_thumb', id_generator(10) + ext)


class UserVideo(models.Model):

    VIDEO_YOUTUBE = 'Y'
    VIDEO_OTHER = 'O'
    VIDEO_VKONTAKTE = 'VK'

    image = models.ImageField('Изображение', upload_to=get_user_video_thumb_path, blank=True, null=True)
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now())
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    url = models.URLField('Ссылка')

    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'

    def get_video_source_type(self):
        if 'youtube' in self.url:
            return self.VIDEO_YOUTUBE
        elif 'vk.com' in self.url:
            return self.VIDEO_VKONTAKTE
        elif self.url:
            return self.VIDEO_OTHER
        else:
            return None

    def download_thumb(self):
        from urllib2 import urlopen
        from django.core.files.base import ContentFile

        try:
            if self.get_video_source_type() == self.VIDEO_YOUTUBE:
                video_id = self.youtube_video_id()
                if video_id:
                    url = 'http://img.youtube.com/vi/%s/hqdefault.jpg' % video_id
                    img = urlopen(url)
                    self.image.save(get_user_video_thumb_path(self, url), ContentFile(img.read()), save=True)

            if self.get_video_source_type() == self.VIDEO_VKONTAKTE:
                from lxml.html.soupparser import fromstring

                response = urlopen(self.url)
                content = response.read()
                doc = fromstring(content)
                preview_img = doc.xpath(r'//img[@id="player_thumb"]')
                if preview_img:
                    url = preview_img[0].get('src')
                    img = urlopen(url)
                    self.image.save(get_user_video_thumb_path(self, url), ContentFile(img.read()), save=True)
        except:
            pass

    def download_thumb_from_url(self, url):
        from urllib2 import urlopen
        from django.core.files.base import ContentFile

        try:
            img = urlopen(url)
            self.image.save(get_user_video_thumb_path(self, url), ContentFile(img.read()), save=True)
        except:
            pass

    def youtube_video_id(self):
        """
        Examples:
        - http://youtu.be/SA2iWivDJiE
        - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        - http://www.youtube.com/embed/SA2iWivDJiE
        - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        """
        from urlparse import urlparse, parse_qs

        try:
            query = urlparse(self.url)
            if query.hostname == 'youtu.be':
                return query.path[1:]
            if query.hostname in ('www.youtube.com', 'youtube.com'):
                if query.path == '/watch':
                    p = parse_qs(query.query)
                    return p['v'][0]
                if query.path[:7] == '/embed/':
                    return query.path.split('/')[2]
                if query.path[:3] == '/v/':
                    return query.path.split('/')[2]
        except:
            pass
        return None

    def get_mime(self):
        from urlparse import urlparse

        query = urlparse(self.url)
        try:
            fname, ext = os.path.splitext(query[2])
            if ext == '.flv':
                return 'video/x-flv'
        except:
            pass
        return 'video/mp4'