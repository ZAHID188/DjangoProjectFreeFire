# Generated by Django 2.1.7 on 2021-09-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameMood', models.CharField(max_length=120)),
                ('map', models.CharField(choices=[('kalahari', 'KALAHARI'), ('bermuda', 'BERMUDA'), ('1', '1')], default='1', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='playerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=120)),
                ('game_id', models.IntegerField()),
            ],
        ),
    ]
