# Generated by Django 4.1.4 on 2023-01-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0011_topic_image_alter_answer_voter_alter_post_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer_reply',
            name='voter',
            field=models.ManyToManyField(blank=True, to='ask.postvoter'),
        ),
    ]