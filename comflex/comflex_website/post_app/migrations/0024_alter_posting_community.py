# Generated by Django 5.0.4 on 2024-05-13 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0023_posttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.community'),
        ),
    ]
