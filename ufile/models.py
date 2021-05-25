# coding=utf8
from django.db import models
import random
import os
import string
from datetime import datetime
from uprofile.models import User


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def get_user_file_path(instance, filename):
    fname, ext = os.path.splitext(filename)
    return os.path.join('user', str(instance.user.id), id_generator(10) + ext)


class UserFile(models.Model):
    name = models.CharField('Название', max_length=250, null=True, blank=True, default='')
    file = models.FileField('Файл', upload_to=get_user_file_path)
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now())
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Файл'
        verbose_name_plural = u'Файлы'
