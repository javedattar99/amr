# Generated by Django 3.0.4 on 2020-06-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_billing_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='report',
            name='meta_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
