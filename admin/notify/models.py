import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class MessageTemplate(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)
    body = models.TextField(_(''), blank=True)

    class Meta:
        verbose_name = _('шаблон')
        verbose_name_plural = _('шаблоны')
        db_table = 'message_template'

    def __str__(self):
        return self.title

class NotifyHistory(TimeStampedModel):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4(), editable=False)
    notification_id = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)
    body = models.TextField(_(''), blank=True)

    class Meta:
        verbose_name = _('шаблон')
        verbose_name_plural = _('шаблоны')
        db_table = 'message_template'

    def __str__(self):
        return self.title
