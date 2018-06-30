# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SiteSetting(models.Model):
	site_title = models.CharField(max_length=200)
	site_logo = models.ImageField(upload_to = 'static/img/', default = 'static/img/logo.jpg')
	site_theme = models.FileField(upload_to = 'static/css/', default = 'static/css/default.css')

class Menu(models.Model):
	menu_name = models.CharField(max_length=200)
	menu_url = models.CharField(max_length=200)

class Banner(models.Model):
	banner_title = models.CharField(max_length=200)
	banner_description = models.TextField(max_length=1023)
	banner_image = models.ImageField(upload_to = 'static/img/', default = 'static/img/banner.jpg')
	banner_button = models.CharField(max_length=200)
	banner_button_url = models.URLField(max_length=200)

class Card(models.Model):
	card_image = models.FileField(upload_to = 'static/icon/', default = 'static/icon/card.svg')
	card_name = models.CharField(max_length=200)
	card_description = models.TextField(max_length=1023)
	card_url = models.URLField(max_length=200)

class Video(models.Model):
	video_title = models.CharField(max_length=200)
	video_description = models.TextField(max_length=1023)
	video_url = models.URLField(max_length=200)
	video_poster = models.ImageField(upload_to = 'static/img/', default = 'static/img/poster.jpg')

class Slider(models.Model):
	slider_image = models.ImageField(upload_to = 'static/img/', default = 'static/img/slider.jpg')
	slider_title = models.CharField(max_length=200)
	slider_url = models.URLField(max_length=200)
		
class Subscribe(models.Model):
	subscribe_title = models.CharField(max_length=200)
	subscribe_description = models.TextField(max_length=1023)
	subscribe_button = models.CharField(max_length=200)
	subscribe_button_url = models.URLField(max_length=200)

class Footer1(models.Model):
	footer_title = models.CharField(max_length=200)
	footer_street = models.TextField(max_length=1023, default = '022')
	footer_district = models.TextField(max_length=1023, default = '022')
	footer_phone = models.CharField(max_length=200, default = '022')
	footer_link_name = models.CharField(max_length=200)
	footer_url = models.URLField(max_length=200)

class Footer2(models.Model):
	footer_title = models.CharField(max_length=200)
	footer_url_name_1 = models.CharField(max_length=200)
	footer_url_1 = models.URLField(max_length=200)
	footer_url_name_2 = models.CharField(max_length=200)
	footer_url_2 = models.URLField(max_length=200)
	footer_url_name_3 = models.CharField(max_length=200)
	footer_url_3 = models.URLField(max_length=200)
	footer_url_name_4 = models.CharField(max_length=200)
	footer_url_4 = models.URLField(max_length=200)

class Footer3(models.Model):
	footer_title = models.CharField(max_length=200)
	footer_url_name_1 = models.CharField(max_length=200)
	footer_url_1 = models.URLField(max_length=200)
	footer_url_name_2 = models.CharField(max_length=200)
	footer_url_2 = models.URLField(max_length=200)
	footer_url_name_3 = models.CharField(max_length=200)
	footer_url_3 = models.URLField(max_length=200)

class Footer4(models.Model):
	footer_title = models.CharField(max_length=200)
	footer_description = models.TextField(max_length=1023)
	footer_end = models.CharField(max_length=200, default = '022')
	footer_link_name = models.CharField(max_length=200)
	footer_url = models.URLField(max_length=200)

