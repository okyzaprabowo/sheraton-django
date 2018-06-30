# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import json

# Create your views here.
def home(request):
	return render(request, 'home.html')

def create_post(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        customer_message = request.POST.get('customer_message')
        response_data = {}

        post = Customer(customer_name=customer_name, customer_phone=customer_phone, customer_message=customer_message)
        post.save()

        response_data['result'] = 'Success'
        return render(request, 'home.html')
        # return HttpResponse(
        #     json.dumps(response_data),
        #     content_type="application/json"
        # )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

