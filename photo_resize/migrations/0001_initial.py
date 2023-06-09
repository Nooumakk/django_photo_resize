# Generated by Django 4.1.7 on 2023-03-24 11:04

from django.db import migrations, models
import photo_resize.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(unique=True, upload_to=photo_resize.models.Photo._load_to)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('slug', models.SlugField(blank=True, max_length=36, unique=True)),
            ],
        ),
    ]
