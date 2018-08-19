# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from polls import models
import datetime
import json
import random
import time


from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world.")

def current_datetime(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

    item_list = list()
    for name in models.Publisher.objects.values_list('name'):
        if len(name) == 1:
            item_list.append(name[0])
        else:
            item_list.append(name)
    # item_list = ['china', 'Jap']
    html_dict = {'current_date': now,
                 'person_name':  'Jimme',
                 'item_list': item_list}
    html_temp = 'polls/current_time.html'

    # html = render(request, html_temp, html_dict)
    # return HttpResponse(html)

    return render_to_response(html_temp, html_dict)


def search_form(request):
    """
    :param request:
    :return: search html
    """
    request.encoding = 'utf-8'
    html_temp = 'polls/search.html'
    return render(request, html_temp)


@csrf_exempt
def search(request):
    request.encoding = 'utf-8'
    print request.GET
    if request.POST:
        message = '你搜索的内容为 by post：' + request.POST['q']
    else:
        message = 'TT你搜索的内容为 by get：' + request.GET['q']
    return HttpResponse(message)


def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def postTest1(request):
    html_temp = 'polls/postTest1.html'
    html = render(request, html_temp)
    return HttpResponse(html)


def postTest2_form(request):
    html_temp = "polls/postTest2.html"
    return render_to_response(html_temp)
    pass


@csrf_exempt
def postTest2(request):
    request.encoding = 'utf-8'
    user = request.POST['user']
    pwd = request.POST['password']
    gender = request.POST['gender']
    hobby = request.POST.getlist('hobby')
    brow = request.POST[u'browser']
    context = {'user': user, 'pwd': pwd, 'gender': gender, 'hobby': hobby, "browser": brow}
    return HttpResponse(json.dumps(context))


def data(request, id):
    rlist = [['Jack', 'Chinese'], ['Mike', 'English'], ['Bob', 'Math'], ['Frank', 'Art'], ['Lucy', 'Music']]
    rlist2 = []
    rlist2.append({"name": rlist[int(id)][0], "subject": rlist[int(id)][1]})
    rjson = json.dumps(rlist2)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(rjson)
    return response


def update(request):
    return render_to_response('polls/update.html')


def ajax(request):
    return render_to_response('polls/ajax_add.html')


# POST VERSION
@csrf_exempt
def ajax_add(request):
    a = int(request.POST['a'])
    b = int(request.POST['b'])
    return_json = {'added': a+b}
    return HttpResponse(json.dumps(return_json), content_type='application/json')


def dyn_echarts(request):
    return render_to_response('polls/dynamic_echarts.html')


@csrf_exempt
def dynecharts_data(request):
    request.encoding = 'utf-8'
    result = dict()
    categories = [u"衬衫",u"羊毛衫",u"雪纺衫",u"裤子",u"高跟鞋",u"袜子"]
    data = []
    for i in range(5):
        data.append(random.randint(10, 50))
    result.update({'categories': categories,
                   'data': data})
    time.sleep(2)
    return HttpResponse(json.dumps(result), content_type='application/json')







