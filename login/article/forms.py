from django.forms import ModelForm
from article.models import Article, Comment

class ArticleForm(ModelForm):
	
	class Meta:
		model = Article
		fields = ('title','body','thumbnail')

class CommentForm(ModelForm):

	class Meta:
		model = Comment
		fields = ('name', 'body')
	