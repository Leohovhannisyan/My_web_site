# Generated by Django 3.2.12 on 2024-03-31 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_usercount'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercount',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]