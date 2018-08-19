# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template  import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost
from django.shortcuts import render, render_to_response

from datetime import datetime
# Create your views here.


def archive(request):
    posts_obj = BlogPost()
    posts_obj.title = "HTML leture"
    posts_obj.content = "format of HTML"
    posts_obj.timestamp = datetime.now()
    posts_obj.save()

    posts = BlogPost.objects.all().order_by("-timestamp")

    # 1st way
    # t2 = loader.get_template('blog/archive.html')
    # t = t2.render({'posts': posts})
    # return HttpResponse(t)

    # 2nd way
    return render_to_response('blog/archive.html', {'posts': posts})


