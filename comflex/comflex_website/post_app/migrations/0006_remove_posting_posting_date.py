# Generated by Django 5.0.4 on 2024-04-23 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0005_community_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='posting_date',
        ),
    ]
