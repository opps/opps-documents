# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from opps.core.admin import apply_opps_rules
from opps.containers.admin import ContainerAdmin
from opps.contrib.multisite.admin import AdminViewPermission

from .forms import DocumentAdminForm


@apply_opps_rules('documents')
class DocumentAdmin(ContainerAdmin, AdminViewPermission):
    form = DocumentAdminForm
    raw_id_fields = ['channel', 'mirror_channel', 'main_image']
    fieldsets = (
        (_(u'Identification'), {
            'fields': ('site', 'title', 'slug', 'get_http_absolute_url',
                       'short_url',)}),
        (_(u'Content'), {
            'fields': ('archive', 'tags')}),
        (_(u'Custom'), {
            'fields': ('json',)}),
        (_(u'Relationships'), {
            'fields': ('channel', 'mirror_channel')}),
        (_(u'Publication'), {
            'classes': ('extrapretty'),
            'fields': ('published', 'date_available',
                       'show_on_root_channel')}),
    )


admin.site.register(Document, DocumentAdmin)
