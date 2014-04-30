# -*- coding:utf-8 -*-

from opps.containers.forms import ContainerAdminForm

from .models import Document


class DocumentAdminForm(ContainerAdminForm):
    class Meta:
        model = Document
