from django.views.generic.edit import FormView
from django.conf import settings
from celery import Celery

from .forms import InputForm

celery = Celery(broker=settings.CELERY_BROKER_URL)


class SendEmail(FormView):
    template_name = 'send_email.html'
    form_class = InputForm
    success_url = '/admin/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.full_clean()

        if form.is_valid():
            data = form.cleaned_data
            task_args = {
              "service": "admin",
              "channel": data["channel"],
              "type": data["type"],
              "payload": {
                "user_id": data["user_id"],
                "body": data.get("body", '')
              }
            }
            celery.send_task(data["channel"], kwargs=task_args)
            return self.form_valid(form)

        return self.form_invalid(form)
