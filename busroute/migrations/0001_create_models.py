# Generated by Django 3.2.17 on 2023-02-13 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busroute.bus')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busroute.route')),
            ],
        ),
    ]
