#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    updatetime = models.DateTimeField(auto_now_add = True)
    
    
    def __unicode__(self):
        return self.title
        
        
class Uni(models.Model):
    title = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40, default=' ')


    def __str__(self):
        return self.name

class Singsong(models.Model):
    title = models.CharField(max_length = 20)
    content = models.CharField(max_length = 60)
    youtubeurl = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.title
        
        
class FreePost(models.Model):
    createuser = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    content = models.TextField()
    updatetime = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(FreePost)
    author = models.CharField(max_length=10)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)