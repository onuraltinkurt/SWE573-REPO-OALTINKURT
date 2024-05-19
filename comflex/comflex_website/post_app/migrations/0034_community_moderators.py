# Generated by Django 5.0.4 on 2024-05-18 22:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0033_posting_dislikes_posting_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='moderated_communities', to=settings.AUTH_USER_MODEL),
        ),
    ]
