# Generated by Django 2.2.3 on 2019-08-01 22:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manyToMany', '0002_auto_20190801_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('biography', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('favourite_genre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='films_watched',
            name='appointment_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 1, 22, 5, 18, 142528, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('length', models.IntegerField()),
                ('summary', models.CharField(max_length=255)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_chapters', to='manyToMany.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Books_Read',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='manyToMany.Book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readers', to='manyToMany.Reader')),
            ],
        ),
        migrations.CreateModel(
            name='Authorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='manyToMany.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_authors', to='manyToMany.Book')),
            ],
        ),
    ]