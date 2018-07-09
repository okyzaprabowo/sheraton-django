# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView 
from homepage.models import *

# Test dari local
def index(request):
	sitesettings = SiteSetting.objects.all()
	banners = Banner.objects.all()
	menus = Menu.objects.all()
	cards = Card.objects.all()
	videos = Video.objects.all()
	sliders = Slider.objects.all()
	subscribes = Subscribe.objects.all()
	footer1s = Footer1.objects.all()
	footer2s = Footer2.objects.all()
	footer3s = Footer3.objects.all()
	footer4s = Footer4.objects.all()
	return render(request, 'index.html',{'sitesettings': sitesettings, 'banners': banners, 'menus' : menus, 'cards': cards,'videos': videos,'sliders': sliders,'subscribes': subscribes,'footer1s': footer1s,'footer2s': footer2s,'footer3s': footer3s,'footer4s': footer4s})