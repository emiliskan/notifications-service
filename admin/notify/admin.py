from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.models import User, Group
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .models import MessageTemplate, NotifyHistory
from .views import SendEmail


@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(NotifyHistory)
class NotifyHistoryAdmin(admin.ModelAdmin):
    pass


class CustomAdminSite(admin.AdminSite):

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        app_list += [
            {
                "name": "Notifications",
                "app_label": "my_test_app",
                "models": [
                    {
                        "name": "Send email",
                        "object_name": "send email",
                        "admin_url": "/admin/send_email",
                        "view_only": True,
                    }
                ],
            }
        ]
        return app_list

    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            url(r'send_email/$', admin.site.admin_view(SendEmail.as_view()), name="send_message")
        ]
        return custom_urls + urls


admin_site = CustomAdminSite(name='admin')
admin_site.register(User)
admin_site.register(Group)
admin_site.register(MessageTemplate)
admin_site.register(NotifyHistory)
admin_site.register(PeriodicTask)
admin_site.register(IntervalSchedule)