from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^index/',views.index,name="index"),
    url(r'^sample2/',views.sample,name='sample'),
]
