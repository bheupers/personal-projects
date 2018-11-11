from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from .models import Post

urlpatterns = [
    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(
                                    model = Post,
                                    template_name="personal/post.html")),
    url(r'^blog$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],
        template_name="personal/blog.html")
        ),
    url(r'^experience$', views.page, kwargs = { 'name' : 'experience'}, name='experience'),

    url(r'^', views.page, kwargs = {'name' : 'overview'}, name='index'),
   ]