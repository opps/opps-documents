# -*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from opps.archives.models import get_file_path
from opps.containers.models import Container


class Document(Container):
    archive = models.FileField(
        upload_to=get_file_path,
        max_length=255,
        verbose_name=_(u'Archive'))

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        ordering = ['-date_available']

    def get_absolute_url(self):
        return self.archive.url
