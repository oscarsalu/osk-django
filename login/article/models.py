# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" %(str(time()).replace('.','_'), filename)

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default = 0)
	thumbnail = models.FileField(upload_to = get_upload_file_name, default = '')

	def __unicode__(self):
		return (self.title)

	def get_absolute_url(self):
		return "/article/get/%i/" % self.id

class Comment(models.Model):
	name = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('Date Commented')
	article = models.ForeignKey(Article)