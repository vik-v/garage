# Generated by Django 4.2rc1 on 2023-03-26 11:22

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Garage name')),
                ('number', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Garage',
                'verbose_name_plural': 'Garages',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Manufacturer name')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='Country')),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('name', models.CharField(max_length=255, verbose_name='Room name')),
                ('floor', models.CharField(choices=[('B', 'Basement'), ('F', 'First floor'), ('S', 'Second floor')], max_length=1, verbose_name='Floor')),
                ('garage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', related_query_name='rooms', to='sensors.garage')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('status', models.BooleanField(verbose_name='Active')),
                ('name', models.CharField(max_length=255, verbose_name='Sensor name')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sensors.manufacturer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', related_query_name='sensors', to='sensors.room')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DHT',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sensors.sensor')),
                ('type', models.CharField(choices=[('DHT', 'Temperature and humidity')], max_length=3, verbose_name='Sensor type')),
                ('temperature', models.FloatField(blank=True, null=True, verbose_name='Temperature')),
                ('humidity', models.FloatField(blank=True, null=True, verbose_name='Humidity')),
            ],
            options={
                'abstract': False,
            },
            bases=('sensors.sensor',),
        ),
        migrations.CreateModel(
            name='PIR',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sensors.sensor')),
                ('type', models.CharField(choices=[('PIR', 'Motin detection')], max_length=3, verbose_name='Sensor type')),
                ('detection', models.BooleanField(verbose_name='Motion detection')),
                ('action_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('sensors.sensor',),
        ),
        migrations.CreateModel(
            name='PR',
            fields=[
                ('sensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sensors.sensor')),
                ('type', models.CharField(choices=[('PR', 'Pressure sensor')], max_length=3, verbose_name='Sensor type')),
                ('pressure', models.FloatField(verbose_name='Pressure')),
            ],
            options={
                'abstract': False,
            },
            bases=('sensors.sensor',),
        ),
    ]
