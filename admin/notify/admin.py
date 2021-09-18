from django.contrib import admin
from .models import MessageTemplate


@admin.register(MessageTemplate)
class MessageTemplate(admin.ModelAdmin):
    pass
    # list_display = ('title', )
    # fields = (
    #     'title', 'description', 'body'
    # )
    # search_fields = ('title', )
