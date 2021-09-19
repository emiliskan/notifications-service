from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.models import User, Group
from .models import MessageTemplate
from .views import SendEmail


@admin.register(MessageTemplate)
class MessageTemplate(admin.ModelAdmin):
    pass
    # list_display = ('title', )
    # fields = (
    #     'title', 'description', 'body'
    # )
    # search_fields = ('title', )


class MyAdminSite(admin.AdminSite):
    def __init__(self, name):
        super(MyAdminSite, self).__init__()

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        print(app_list)
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
                    },
                    {
                        "name": "Send periodic emails",
                        "object_name": "send periodic emails",
                        "admin_url": "/admin/send_periodic_emails",
                        "view_only": True,
                    }
                ],
            }
        ]
        return app_list

    def get_urls(self):

        urls = super().get_urls()
        urls += [
            url(r'^send_email/$',
                admin.site.admin_view(SendEmail.as_view()))
        ]
        return urls


admin_site = MyAdminSite(name='admin')
admin_site.register(User)
admin_site.register(Group)
