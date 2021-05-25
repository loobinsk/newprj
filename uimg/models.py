# coding=utf8
from django.db import models
import random
import os
import string
from datetime import datetime
from uprofile.models import User
import urllib2
from django.core.files.base import ContentFile
from PIL import Image
import traceback
import requests


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def get_user_avatar_path(instance, filename):
    fname, ext = os.path.splitext(filename)
    gen_id = id_generator(10)
    return os.path.join('user', str(instance.id), gen_id[:3], id_generator(10) + ext)


def get_user_image_path(instance, filename):
    fname, ext = os.path.splitext(filename)
    if (not ext) or ('php' in ext):
        ext = '.jpg'
    if hasattr(instance, 'user'):
        user_id = instance.user.id if instance.user else 0
    else:
        user_id = 0
    gen_id = id_generator(10)
    return os.path.join('user', str(user_id), gen_id[:3], gen_id + ext)


class UserImage(models.Model):
    image = models.ImageField('Изображение', upload_to=get_user_image_path)
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now())
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    desc = models.TextField('Описание', max_length=250, default='', blank=True, null=True)

    class Meta:
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'

    @property
    def is_animated(self):
        if self.image:
            fileName, fileExtension = os.path.splitext(self.image.path)
            return fileExtension in ['.gif', '.webp']
        else:
            return False

    def load_image(self, href, logger=None):
        try:
            r = requests.get(href, timeout=10)
            f = ContentFile(r.content)
            self.image.save(get_user_image_path(self, href.split('?')[0]), f, save=True)
            return True
        except:
            if logger:
                logger.info(traceback.format_exc())
            return False

    def load_image_crop(self, href):
        try:
            self.load_image(href)
            image = Image.open(self.image.path)
            width, height = image.size
            image.crop((0, 100, width, height-67)).save(self.image.path)
            return True
        except:
            return False

    def load_image_cian_crop(self, href):
        try:
            self.load_image(href)
            image = Image.open(self.image.path)
            width, height = image.size
            image.crop((0, 100, width, height-144)).save(self.image.path)
            return True
        except:
            return False

    def load_image_avito_crop(self, href, logger=None):
        try:
            self.load_image(href)
            image = Image.open(self.image.path)
            width, height = image.size
            image.crop((0, 0, width, height-50)).save(self.image.path)
            return True
        except Exception, err:
            if logger:
                logger.info(traceback.format_exc())
            return False

    def load_image_domofond_crop(self, href, logger=None):
        try:
            self.load_image(href)
            image = Image.open(self.image.path)
            width, height = image.size
            image.crop((0, 50, width, height)).save(self.image.path)
            return True
        except Exception, err:
            if logger:
                logger.info(traceback.format_exc())
            return False

    def load_image_irr_crop(self, href):
        try:
            self.load_image(href)
            image = Image.open(self.image.path)
            width, height = image.size
            image.crop((0, 0, width, height-150)).save(self.image.path)
            return True
        except Exception, err:
            print(traceback.format_exc())
            return False

    def load_image_chance_crop(self, href):
        try:
            self.load_image(href)
            image = Image.open(self.image.path)
            width, height = image.size
            image.crop((0, 0, width, height-80)).save(self.image.path)
            return True
        except Exception, err:
            print(traceback.format_exc())
            return False

    def save(self, *args, **kwargs):
        if not self.id and self.image.name:
            from main.models import SyncFiles
            SyncFiles.syncfiles([self.image.name])
        return super(UserImage, self).save(*args, **kwargs)