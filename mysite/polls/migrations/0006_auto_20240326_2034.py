# Generated by Django 3.2.12 on 2024-03-26 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20240326_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='polluser',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polluser',
            name='city',
            field=models.CharField(default='Default city', max_length=120),
        ),
        migrations.AddField(
            model_name='polluser',
            name='country',
            field=models.CharField(default='Default country', max_length=120),
        ),
    ]
