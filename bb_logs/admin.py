# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from bb_logs.models import Bb_operation, Bb_base, Bb_url, Bb_operation_dday


# Register your models here.
admin.site.register(Bb_operation)
admin.site.register(Bb_base)
admin.site.register(Bb_url)
admin.site.register(Bb_operation_dday)
