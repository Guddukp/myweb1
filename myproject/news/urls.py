from django.conf.urls import url
from . import views
urlpatterns = [
     url(r'^news/(?p<pk>\d+)/$', views.news_detail , name='news_detail'),
]