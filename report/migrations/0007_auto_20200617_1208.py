# Generated by Django 3.0.4 on 2020-06-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_auto_20200608_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
