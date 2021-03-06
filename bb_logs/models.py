# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bb_operation(models.Model):
	""" Task Force Operations """
	title = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		""" Return a string representation of the model."""
		return self.title

class Bb_base(models.Model):
	""" Task Force Operations """
	name = models.CharField(max_length=200)
	bb_operation = models.ForeignKey(Bb_operation, models.SET_NULL,blank=True,null=True,)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		""" Return a string representation of the model."""
		basestring=str(self.bb_operation)+"........"+str(self.name)
		return basestring

		
class Bb_url(models.Model):
	""" Task Force Operations """
	bb_base = models.ForeignKey(Bb_base, models.SET_NULL,blank=True,null=True,)
	bb_operation = models.ForeignKey(Bb_operation, models.SET_NULL,blank=True,null=True,)
	bb_url = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		""" Return a string representation of the model."""
		urlstring=str(self.bb_base)+".."+str(self.bb_url)	
		return urlstring
		#return self.url

class Bb_operation_dday(models.Model):
	""" todays operation """
	bb_base = models.ForeignKey(Bb_base, models.SET_NULL,blank=True,null=True,)
	bb_operation = models.ForeignKey(Bb_operation, models.SET_NULL,blank=True,null=True,)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		""" Return a string representation of the model."""
		stri=str(self.bb_base)
		return self.bb_base