# Generated by Django 4.2.11 on 2024-09-24 17:56

import django.utils.timezone

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("actionlog", "0003_existing_pretranslation_action"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actionlog",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
