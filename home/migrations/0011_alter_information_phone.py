# Generated by Django 5.0.1 on 2024-01-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_information_mainpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='phone',
            field=models.CharField(max_length=14),
        ),
    ]
