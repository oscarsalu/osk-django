# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
#from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context 
from django.views.generic.base import TemplateView
from article.models import Article
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
# Create your views here.

# def hello(request):
# 	name = "oscar"
# 	context = {'name': name }
# 	return render(request,'hello.html', context)

#create view with class

# class HelloTemplate(TemplateView):
# 	"""docstring for HelloTemplate"""
# 	template_name = 'hello.html'
# 	def get_context_data(self, **kwargs):
# 		context = super(HelloTemplate, self).get_context_data(**kwargs)
# 		context['name'] = 'oscar'
# 		return context

def articles(request):

	language = 'en-us'
	session_language = 'en-us'

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']

	context = {'articles': Article.objects.all(), 'language' : language , 'session_language' : session_language}
	return render_to_response('articles.html', context)

def article(request, article_id = 1):
	context = {'article': Article.objects.get(id=article_id)}
	return render_to_response('article.html', context) 

def language(request, language='en-us'):
	response = HttpResponse("Setting language to %s" % language)

	response.set_cookie('lang', language)
	request.session['lang'] = language
	return response
#to create a article ,to save to the database
#first check if the request is a POST request
def create(request):
	if request.POST:
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/article/all')
	else:
		form = ArticleForm()

	a = {}
	a.update(csrf(request))

	a['form'] = form

	return render_to_response('create_article.html' ,a)