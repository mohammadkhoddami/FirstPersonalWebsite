# Generated by Django 5.0.1 on 2024-01-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_projects_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exprience',
            name='job_description',
            field=models.CharField(max_length=1150),
        ),
    ]