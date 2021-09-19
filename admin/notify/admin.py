from django.contrib import admin
from django.conf.urls import url
# from django.contrib.auth.models import User, Group
from .models import MessageTemplate, NotifyHistory
from .views import SendEmail


@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(NotifyHistory)
class NotifyHistoryAdmin(admin.ModelAdmin):
    pass


class MyAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        custom_urls = [
            url(r'send_email/$', admin.site.admin_view(SendEmail.as_view()), name="send_message")
        ]
        return urls + custom_urls


admin_site = MyAdminSite(name='admin')
# admin_site.register(User)
# admin_site.register(Group)
