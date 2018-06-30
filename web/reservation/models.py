# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
	customer_name = models.CharField(max_length=200)
	customer_phone = models.CharField(max_length=200)
	customer_message = models.TextField(max_length=1023)
