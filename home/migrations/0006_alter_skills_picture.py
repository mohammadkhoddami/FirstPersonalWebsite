# Generated by Django 5.0.1 on 2024-01-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_education_ended_at_alter_education_started_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='picture',
            field=models.ImageField(upload_to='cv_picture'),
        ),
    ]