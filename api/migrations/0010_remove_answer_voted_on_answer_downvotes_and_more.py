# Generated by Django 4.0 on 2021-12-19 18:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_merge_20211219_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='voted_on',
        ),
        migrations.AddField(
            model_name='answer',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='downvoted_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='upvoted_answers', to=settings.AUTH_USER_MODEL),
        ),
    ]