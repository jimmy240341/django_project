# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'timestamp')


admin.site.register(BlogPost, BlogPostAdmin)

