# Generated by Django 3.2.12 on 2024-04-08 18:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0021_polluser_subscription'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PollUser',
            new_name='FriendFusionUser',
        ),
    ]