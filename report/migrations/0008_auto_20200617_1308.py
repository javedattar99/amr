# Generated by Django 3.0.4 on 2020-06-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_auto_20200617_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
