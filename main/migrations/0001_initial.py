# Generated by Django 3.1 on 2020-08-29 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_id', models.CharField(max_length=50)),
                ('aircraft_type', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ICAO_code', models.CharField(max_length=50)),
                ('IATA_code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company_function', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('remarks', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('block_out', models.TimeField()),
                ('block_in', models.TimeField()),
                ('landings', models.IntegerField()),
                ('take_off', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255)),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.aircraft')),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='main.airport')),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='main.airport')),
                ('pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.people')),
            ],
        ),
    ]