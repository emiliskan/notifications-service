# Generated by Django 3.1 on 2021-09-19 18:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0002_auto_20210919_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplate',
            name='type',
            field=models.CharField(choices=[('email', 'Email'), ('sms', 'Sms'), ('websocket', 'Websocket')], default='email', max_length=20, verbose_name='тип сообщения'),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='body',
            field=models.TextField(blank=True, verbose_name='шаблон'),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='description',
            field=models.TextField(blank=True, max_length=255, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='id',
            field=models.UUIDField(default=uuid.UUID('682971cf-c60b-4f45-8e70-2750e5bafdfb'), editable=False, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='title',
            field=models.CharField(max_length=80, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='notifyhistory',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0ec589aa-f2a1-4ae6-b11e-7fc1cc793870'), editable=False, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
