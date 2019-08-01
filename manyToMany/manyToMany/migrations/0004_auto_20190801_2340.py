# Generated by Django 2.2.3 on 2019-08-01 23:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manyToMany', '0003_auto_20190801_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='films_watched',
            name='appointment_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 1, 23, 40, 27, 926404, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('comic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comics', to='manyToMany.Comic')),
            ],
        ),
        migrations.CreateModel(
            name='Comic_Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comics_writer', to='manyToMany.Comic')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writers_comic', to='manyToMany.Writer')),
            ],
        ),
        migrations.CreateModel(
            name='Comic_Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists_comic', to='manyToMany.Artist')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comics_artist', to='manyToMany.Comic')),
            ],
        ),
    ]
