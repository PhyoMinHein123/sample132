#urls.py
from django.urls import path
from my_blog.views import postlist, postcreate

urlpatterns = [
	path('list/', postlist),
	path('create/', postcreate)
]