# Generated by Django 4.1.4 on 2023-01-16 07:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('tag', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]