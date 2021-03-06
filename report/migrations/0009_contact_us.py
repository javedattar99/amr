# Generated by Django 3.0.4 on 2020-06-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_auto_20200617_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('corporate_email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact_Us',
            },
        ),
    ]
