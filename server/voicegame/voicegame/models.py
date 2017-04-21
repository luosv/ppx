# -*- coding: utf-8 -*-
from django.db import models


class Log(models.Model):
    name = models.CharField(max_length=128)
    score = models.IntegerField(default=0)
    ip = models.CharField(max_length=64, blank=True)
    tag = models.CharField(max_length=16, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    num = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
