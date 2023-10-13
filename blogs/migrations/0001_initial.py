# Generated by Django 4.2.5 on 2023-10-13 11:39

from django.db import migrations, models
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, max_length=1500, null=True)),
                ('video', models.FileField(default=None, upload_to='videos/')),
                ('thumbnail', models.ImageField(default='previews/defaultpreview.png', max_length=512, upload_to='previews/')),
                ('is_published', models.BooleanField(default=True)),
                ('views', models.PositiveIntegerField(default=0, verbose_name='views')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'ordering': ['-pub_date', '-mod_date'],
            },
            managers=[
                ('videoobjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('body', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-pub_date', '-mod_date'],
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Название Плейлиста')),
                ('description', models.TextField(blank=True, max_length=1500, null=True)),
                ('thumbnail', models.ImageField(default='previews/defaultpreview.png', max_length=512, upload_to='previews/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Плейлист',
                'verbose_name_plural': 'Плейлист',
                'ordering': ['-pub_date'],
            },
        ),
    ]
