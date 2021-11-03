# Generated by Django 3.2.7 on 2021-11-04 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211104_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='the_comment',
        ),
        migrations.AddField(
            model_name='feedback',
            name='the_feedback',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
