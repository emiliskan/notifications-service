from django import forms

from .models import MessageTemplate

CHANNEL_CHOICES = (('email', 'email'),)


class InputForm(forms.Form):
    channel = forms.CharField(widget=forms.Select(choices=CHANNEL_CHOICES), required=True)
    recipient = forms.CharField(widget=forms.TextInput, required=False, max_length=250)
    subject = forms.CharField(widget=forms.TextInput, required=False, max_length=250)
    user_id = forms.CharField(max_length=250, required=True)
    body = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        message_type_objects = MessageTemplate.objects.all().values_list('type', flat=True)

        # dynamically update message types Dropdown
        message_types = ((mes_type, mes_type) for mes_type in message_type_objects)
        self.fields['type'] = forms.CharField(widget=forms.Select(choices=message_types), required=True)
