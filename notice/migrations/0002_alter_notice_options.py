# Generated by Django 4.1.4 on 2023-01-18 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-date_posted']},
        ),
    ]