import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class MessageTemplateType(models.TextChoices):
    email = 'email'
    sms = 'sms'
    websocket = 'websocket'


class MessageTemplate(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4(), editable=False)
    channel = models.CharField(_('способ связи'),  max_length=20,
                               choices=MessageTemplateType.choices,
                               default=MessageTemplateType.email)
    type = models.CharField(_('тип сообщения'), max_length=80)
    title = models.CharField(_('название'), max_length=80)
    description = models.CharField(_('описание'), max_length=255, blank=True)
    body = models.TextField(_('шаблон'))

    class Meta:
        verbose_name = _('шаблон')
        verbose_name_plural = _('шаблоны')
        db_table = 'message_template'

    def __str__(self):
        return self.title


# TODO set all fields editable=False
class NotifyHistory(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4(), editable=False)
    service = models.CharField(_('источник'), max_length=80, null=True)
    channel = models.CharField(_('способ связи'),  max_length=20,
                               choices=MessageTemplateType.choices,
                               default=MessageTemplateType.email)
    type = models.CharField(_('тип сообщения'), max_length=80, null=True)
    send_time = models.DateField(_('дата отправки'), null=True)
    body = models.TextField(_('текст сообщения'), blank=True)

    class Meta:
        verbose_name = _('история оповещений')
        verbose_name_plural = _('история оповещений')
        db_table = 'message_history'

    def __str__(self):
        return self.service
