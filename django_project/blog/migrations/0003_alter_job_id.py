# Generated by Django 5.0.3 on 2024-04-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_job_agency_remove_job_job_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
