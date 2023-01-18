# Generated by Django 4.1.4 on 2023-01-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.CharField(default='token will  genrated in feature', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Staf', 'Staf'), ('Student', 'Student'), ('Unknow', 'Unknow')], default='Staf', max_length=255),
        ),
    ]