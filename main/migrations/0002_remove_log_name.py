# Generated by Django 3.1 on 2020-08-29 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='name',
        ),
    ]