# Generated by Django 5.0.3 on 2024-04-15 03:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_job_actual_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='actual_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
