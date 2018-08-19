# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def home(request):
    # tutoriallist = ['HTML', 'CSS', 'JS', 'PYTHON', 'DJANGO']
    # tutoriallist = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    # t = map(str, range(10))
    # t = ['1', '2', '3','4']
    t = list()
    return render(request, 'home.html', {'tutoriallist': t})
