# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
#from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context 
from django.views.generic.base import TemplateView
from article.models import Article, Comment
from forms import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.utils import timezone
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

	a = {}
	a.update(csrf(request))

	a['articles'] =Article.objects.all()
	a['language'] = language
	a['session_language'] = session_language

	return render_to_response('articles.html', a)

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
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			c = form.save(commit=False)
			c.pub_date = timezone.now()
			c.save()

			return HttpResponseRedirect('/article/all')
	else:
		form = ArticleForm()

	a = {}
	a.update(csrf(request))

	a['form'] = form

	return render_to_response('create_article.html' ,a)

def like_article(request, article_id):
	if article_id:
		a= Article.objects.get(id = article_id)
		count = a.likes
		count += 1
		a.likes = count
		a.save()

	return HttpResponseRedirect('/article/get/%s' % article_id)

def add_comment(request, article_id):
	a = Article.objects.get(id=article_id)

	if request.method == "POST":
		f = CommentForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.pub_date = timezone.now()
			c.article = a
			c.save()

			return HttpResponseRedirect('/article/get/%s' % article_id)
	else:
		f = CommentForm()

	b = {}
	b.update(csrf(request))

	b['article'] = a
	b['form'] = f

	return render_to_response('add_comment.html', b)
	
def search_titles(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
	
	articles = Article.objects.filter(title__contains=search_text)

	return render_to_response('ajax_search.html',{'articles': articles})