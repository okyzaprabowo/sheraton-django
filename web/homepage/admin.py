# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SiteSetting, Menu, Banner, Video, Slider, Card, Subscribe, Footer1, Footer2, Footer3, Footer4

# Register your models here.
class SiteSettingAdmin(admin.ModelAdmin):
	list_display = ('site_title', 'site_logo', 'site_theme')
	fields = ['site_title', 'site_logo', 'site_theme']
	def has_add_permission(self,request):
		return False

class MenuAdmin(admin.ModelAdmin):
	list_display = ('menu_name', 'menu_url')
	fields = ['menu_name', 'menu_url']

class BannerAdmin(admin.ModelAdmin):
	list_display = ('banner_title', 'banner_description', 'banner_image', 'banner_button')
	fields = ['banner_title', 'banner_description', 'banner_image', 'banner_button']
	def has_add_permission(self,request):
		return False

class CardAdmin(admin.ModelAdmin):
	list_display = ('card_name', 'card_description', 'card_image')
	fields = ['card_name', 'card_description', 'card_image']
	def has_add_permission(self,request):
		return False

class VideoAdmin(admin.ModelAdmin):
	list_display = ('video_title', 'video_description', 'video_url', 'video_poster')
	fields = ['video_title', 'video_description', 'video_url', 'video_poster']
	def has_add_permission(self,request):
		return False

class SliderAdmin(admin.ModelAdmin):
	list_display = ('slider_image', 'slider_title', 'slider_url')
	fields = ['slider_image', 'slider_title', 'slider_url']
	def has_add_permission(self,request):
		return False

class SubscribeAdmin(admin.ModelAdmin):
	list_display = ('subscribe_title', 'subscribe_description', 'subscribe_button', 'subscribe_button_url')
	fields = ['subscribe_title', 'subscribe_description', 'subscribe_button', 'subscribe_button_url']
	def has_add_permission(self,request):
		return False

class Footer1Admin(admin.ModelAdmin):
	list_display = ('footer_title', 'footer_street', 'footer_district', 'footer_phone', 'footer_link_name' ,'footer_url')
	fields = ['footer_title', 'footer_street', 'footer_district', 'footer_phone', 'footer_link_name', 'footer_url']
	def has_add_permission(self,request):
		return False

class Footer2Admin(admin.ModelAdmin):
	list_display = ('footer_title', 'footer_url_name_1', 'footer_url_1', 'footer_url_name_2', 'footer_url_2', 'footer_url_name_3', 'footer_url_3', 'footer_url_name_4', 'footer_url_4')
	fields = ['footer_title', 'footer_url_name_1', 'footer_url_1', 'footer_url_name_2', 'footer_url_2', 'footer_url_name_3', 'footer_url_3', 'footer_url_name_4', 'footer_url_4']
	def has_add_permission(self,request):
		return False

class Footer3Admin(admin.ModelAdmin):
	list_display = ('footer_title', 'footer_url_name_1', 'footer_url_1', 'footer_url_name_2', 'footer_url_2', 'footer_url_name_3', 'footer_url_3')
	fields = ['footer_title', 'footer_url_name_1', 'footer_url_1', 'footer_url_name_2', 'footer_url_2', 'footer_url_name_3', 'footer_url_3']
	def has_add_permission(self,request):
		return False

class Footer4Admin(admin.ModelAdmin):
	list_display = ('footer_title', 'footer_description', 'footer_link_name', 'footer_url', 'footer_end')
	fields = ['footer_title', 'footer_description', 'footer_link_name', 'footer_url', 'footer_end']
	def has_add_permission(self,request):
		return False

admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Footer1, Footer1Admin)
admin.site.register(Footer2, Footer2Admin)
admin.site.register(Footer3, Footer3Admin)
admin.site.register(Footer4, Footer4Admin)