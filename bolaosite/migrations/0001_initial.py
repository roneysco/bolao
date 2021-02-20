# Generated by Django 3.1.7 on 2021-02-20 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('time1', models.CharField(max_length=200)),
                ('time2', models.CharField(max_length=200)),
                ('data_hora', models.CharField(max_length=200)),
                ('gols_time1', models.IntegerField(blank=True, null=True, verbose_name='gols_time1')),
                ('gols_time2', models.IntegerField(blank=True, null=True, verbose_name='gols_time1')),
            ],
        ),
    ]
