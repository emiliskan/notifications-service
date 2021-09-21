from django import forms

from .models import MessageTemplate

CHANNEL_CHOICES = (('email', 'email'),)
message_type_objects = MessageTemplate.objects.all().values_list('type', flat=True)
MESSAGE_TYPES = ((mes_type, mes_type) for mes_type in message_type_objects)


class InputForm(forms.Form):
    user_id = forms.CharField(max_length=250)
    channel = forms.CharField(widget=forms.Select(choices=CHANNEL_CHOICES))
    type = forms.CharField(widget=forms.Select(choices=MESSAGE_TYPES))
