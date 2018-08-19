# -*- coding: utf-8 -*-

from django.conf.urls import url
from learn import views as learn_views

urlpatterns = [
    url('^$', learn_views.home, name='home'),
]