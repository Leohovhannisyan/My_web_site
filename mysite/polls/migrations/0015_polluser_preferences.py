# Generated by Django 3.2.12 on 2024-04-03 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_delete_usercount'),
    ]

    operations = [
        migrations.AddField(
            model_name='polluser',
            name='preferences',
            field=models.CharField(default='No prefrences yet', max_length=120),
        ),
    ]
