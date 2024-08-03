# Generated by Django 5.0.7 on 2024-08-03 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartwatch',
            fields=[
                ('imei', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('bpm', models.IntegerField()),
                ('mmhg', models.CharField(max_length=10)),
                ('temperatura_corporal', models.CharField(max_length=8)),
                ('funcionario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='smartwatch', to='funcionarios.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='SmartwatchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('bpm', models.IntegerField()),
                ('mmhg', models.CharField(max_length=10)),
                ('temperatura_corporal', models.CharField(max_length=8)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('smartwatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico', to='smartwatches.smartwatch')),
            ],
        ),
    ]