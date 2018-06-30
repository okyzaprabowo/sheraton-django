# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('customer_name', 'customer_phone', 'customer_message')
	fields = ['customer_name', 'customer_phone', 'customer_message']
	def has_add_permission(self,request):
		return False

admin.site.register(Customer, CustomerAdmin)
