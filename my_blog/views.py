from django.shortcuts import render
from my_blog.models import *


def postlist(request):
	posts = PostModel.objects.all()
	return render(request, 'postlist.html',{'posts':posts})

def postcreate(request):
	if request.method == "GET":
		category = CategoryModel.objects.all()
		return render(request, 'postcreate.html',{'category':category})