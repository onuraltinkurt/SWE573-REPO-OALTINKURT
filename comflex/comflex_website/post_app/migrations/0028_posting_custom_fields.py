# Generated by Django 5.0.4 on 2024-05-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0027_posttypefield_is_fixed'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='custom_fields',
            field=models.JSONField(default=dict),
        ),
    ]
