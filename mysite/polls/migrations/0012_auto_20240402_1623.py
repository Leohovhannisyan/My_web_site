# Generated by Django 3.2.12 on 2024-04-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='polluser',
            name='user_image',
            field=models.ImageField(default='default image', upload_to=''),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='user_image',
            field=models.ImageField(default='defualt img', upload_to=''),
        ),
    ]