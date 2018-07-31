# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=30)

    def __unicode__(self):
        return "{}-token".format(self.user)


class Expense(models.Model):
    text = models.CharField(max_length=255)
    time = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{}-{}".format(self.time, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=255)
    time = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{}-{}".format(self.time, self.amount)