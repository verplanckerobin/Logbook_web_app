# Generated by Django 3.1 on 2020-09-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_log_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='notes',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]