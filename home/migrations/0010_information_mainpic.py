# Generated by Django 5.0.1 on 2024-01-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_cvprofile_bio_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='MainPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='cv_picture')),
            ],
        ),
    ]
