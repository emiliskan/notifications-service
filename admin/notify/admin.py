from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.models import User, Group
from .models import MessageTemplate
from .views import SendEmail


@admin.register(MessageTemplate)
class MessageTemplate(admin.ModelAdmin):
    pass


