# Generated by Django 4.1.4 on 2023-01-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_auth_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='i_answer',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='i_question',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='token will  genrated in feature', max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Staf', 'Staf'), ('Student', 'Student'), ('Unknow', 'Unknow')], default='Staf', max_length=255),
        ),
    ]