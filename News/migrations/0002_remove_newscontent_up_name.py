# Generated by Django 3.1.4 on 2020-12-18 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newscontent',
            name='up_name',
        ),
    ]
