# Generated by Django 3.2.7 on 2021-09-19 13:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetemplate',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0eb7fa1e-6aec-4053-91fa-f3fe4619814c'), editable=False, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='notifyhistory',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e4af4a6c-75c0-4ff6-a92f-98cf45916b76'), editable=False, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
