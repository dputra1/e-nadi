# Generated by Django 3.2.7 on 2021-11-03 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='the_comment',
            new_name='the_feedback',
        ),
    ]