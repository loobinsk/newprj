# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class SyncFiles(models.Model):
    """
    Синхронизатор файлов
    """
    SERVER1 = 1
    SERVER2 = 2
    SERVER1_PATH = ''
    SERVER2_PATH = ''

    files = models.TextField(verbose_name='Файлы', default='')
    server = models.IntegerField(verbose_name='Расположение', default=SERVER1)

    class Meta:
        verbose_name = 'Файлы для синхронизации'
        verbose_name_plural = 'Файлы для синхронизации'

    def __unicode__(self):
        return unicode(self.id)

    def addfile(self, filename):
        list = self.files.split(';')
        list.append(filename)
        self.files = ';'.join(list)

    def getfiles(self):
        return self.files.split(';')

    def save(self, *args, **kwargs):
        if not self.id:
            self.server = settings.SERVER_ID
        return super(SyncFiles, self).save(*args, **kwargs)

    @staticmethod
    def sync():
        from tempfile import NamedTemporaryFile
        import subprocess
        import os

        # синхронизация с мастера на ведомый
        sync_list = SyncFiles.objects.filter(server=SyncFiles.SERVER1)
        file_list = []
        item_ids = []
        for item in sync_list:
            file_list += item.getfiles()
            item_ids.append(item.id)

        if file_list:
            with NamedTemporaryFile(delete=False) as f:
                f.write('\n'.join(file_list))
                f.close()
                subprocess.call(['rsync', '-zur', '--files-from=%s' % f.name, SyncFiles.SERVER1_PATH,  SyncFiles.SERVER2_PATH])
                os.unlink(f.name)
                SyncFiles.objects.filter(id__in=item_ids).delete()

         # синхронизация с ведомого на мастер
        sync_list = SyncFiles.objects.filter(server=SyncFiles.SERVER2)
        file_list = []
        item_ids = []
        for item in sync_list:
            file_list += item.getfiles()
            item_ids.append(item.id)

        if file_list:
            with NamedTemporaryFile(delete=False) as f:
                f.write('\n'.join(file_list))
                f.close()
                subprocess.call(['rsync', '-zur', '--files-from=%s' % f.name, SyncFiles.SERVER2_PATH,  SyncFiles.SERVER1_PATH])
                os.unlink(f.name)
                SyncFiles.objects.filter(id__in=item_ids).delete()

    @staticmethod
    def syncfiles(filelist=[]):
        # if filelist:
        #     item = SyncFiles(files=';'.join(filelist))
        #     item.save()
        pass


