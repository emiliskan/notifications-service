from django.views.generic.edit import FormView
from celery import Celery

from config.settings import base as config
from .forms import InputForm

celery = Celery(broker=config.CELERY_BROKER_URL)


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
            print(data)
            # celery.send_task('send_email', list(data.values()))
            return self.form_valid(form)

        return self.form_invalid(form)


class SendPeriodicEmail(FormView):
    template_name = 'send_periodic_email.html'
    form_class = InputForm
    success_url = '/admin/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.full_clean()

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return self.form_valid(form)

        return self.form_invalid(form)