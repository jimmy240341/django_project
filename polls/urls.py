# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'dynechart/dynechart_data/$', views.dynecharts_data, name='dynecharts_data'),
    url(r'dynechart/$', views.dyn_echarts, name='dyn_echarts'),
    url(r'ajax/add/$', views.ajax_add, name='ajax_add'),
    url(r'ajax/$', views.ajax, name='ajax'),
    url(r'^data/(?P<id>\d+)/$', views.data, name='data'),
    url(r'^update/', views.update),
    url(r'postTest2_form/postTest2', views.postTest2, name='postTest2'),
    url(r'postTest2_form/$', views.postTest2_form, name='postTest2_form'),
    url(r'search_form/search/$', views.search, name='search'),
    url(r'search_form/$', views.search_form, name='search_form'),
    url(r'time/plus/(\d{1,2})/$', views.hours_ahead, name='hours_ahead'),
    url(r'^time/$', views.current_datetime, name='time'),
    url(r'^$', views.current_datetime, name='current_datetime')
]

