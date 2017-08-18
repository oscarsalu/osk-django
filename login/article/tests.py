# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from article.models import Article, get_upload_file_name
from django.utils import timezone
from time import time
# Create your tests here.

class ArticleTest(TestCase):
	def create_article(self, title="test article", body="Blah Blah Blah"):
		return Article.objects.create(title = title,
									  body = body,
									  pub_date = timezone.now(),
									  likes = 0)
	def test_article_creation(self):
		a = self.create_article()
		self.assertTrue(isinstance(a, Article))
		self.assertEqual(a.__unicode__(), a.title)

	def test_get_upload_file_name(self):
		filename = "testname.jpg"
		path = "uploaded_files/%s_%s" %(str(time()).replace('.','_'), filename)

		created_path = get_upload_file_name(self, filename)

		self.assertEqual(path, created_path)