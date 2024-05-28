# Generated by Django 4.2.7 on 2024-02-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_cvprofile_cvfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
