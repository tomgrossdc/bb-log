# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Bb_base, Bb_url

# Create your views here.
def index(request):
	""" home page of bb_logs """
	return render(request, 'bb_logs/index.html')

def bb_bases(request):
	bb_bases = Bb_base.objects.order_by('bb_operation','name')
	context = {'bb_bases': bb_bases}
	return render(request, 'bb_logs/bb_bases.html', context)

def bb_urls(request):
	bb_urls = Bb_url.objects.order_by('bb_operation','bb_base')
	context = {'bb_urls': bb_urls}
	return render(request, 'bb_logs/bb_urls.html', context)
	