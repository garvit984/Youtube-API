# Generated by Django 3.2.7 on 2021-09-07 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='author',
            new_name='channelTitle',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='publish_datetime',
            new_name='publishTime',
        ),
    ]
