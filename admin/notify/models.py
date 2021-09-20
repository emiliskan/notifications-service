import uuid
from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class MessageTemplateType(models.TextChoices):
    email = 'email'
    sms = 'sms'
    websocket = 'websocket'


CHANNEL = models.CharField(_('способ связи'),  max_length=20,
                           choices=MessageTemplateType.choices,
                           default=MessageTemplateType.email)


class MessageTemplate(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4(), editable=False)
    channel = CHANNEL
    type = models.CharField(_('тип сообщения'), max_length=80, default='')
    sender = models.CharField(_('отправитель'), max_length=80, default='admin')
    description = models.CharField(_('описание'), max_length=255, blank=True)
    body = models.TextField(_('шаблон'))

    class Meta:
        verbose_name = _('шаблон')
        verbose_name_plural = _('шаблоны')
        db_table = 'message_template'
        unique_together = ('channel', 'type',)

    def __str__(self):
        return self.type


class NotifyHistory(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4())
    service = models.CharField(_('источник'), max_length=80, default='admin')
    channel = CHANNEL
    type = models.CharField(_('тип сообщения'), max_length=80, default='email')
    recipient = models.CharField(_('получатель'), max_length=80, default='nobody@email.com')
    send_time = models.DateTimeField(_('дата отправки'), default=datetime.now)
    body = models.TextField(_('текст сообщения'))

    class Meta:
        verbose_name = _('история оповещений')
        verbose_name_plural = _('история оповещений')
        db_table = 'message_history'

    def __str__(self):
        return self.service

    def has_change_permission(self, request, obj=None):
        return False
