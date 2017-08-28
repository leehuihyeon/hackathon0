#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post, Uni, User, Singsong
# Register your models here.
admin.site.register(Post)
admin.site.register(Uni)
admin.site.register(User)
admin.site.register(Singsong)