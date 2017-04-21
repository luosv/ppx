from django.contrib import admin
from voicegame import models


class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'score', 'ip', 'tag', 'create_time']


admin.site.register(models.Log, LogAdmin)
