# Generated by Django 4.0.1 on 2022-02-01 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postmodel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ['-created_at']},
        ),
    ]
