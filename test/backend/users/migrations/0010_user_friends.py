# Generated by Django 3.2.10 on 2024-04-29 16:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20240427_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='added_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
