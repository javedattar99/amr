# Generated by Django 3.0.4 on 2020-06-05 01:49

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='reportimage/')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='publishers/')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('meta_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('summary', ckeditor.fields.RichTextField()),
                ('tabel_of_content', ckeditor.fields.RichTextField()),
                ('published_date', models.DateField(auto_now_add=True)),
                ('no_of_pages', models.IntegerField(default=100)),
                ('single_user_price', models.IntegerField(default=2000)),
                ('multi_user_price', models.IntegerField(default=4000)),
                ('corporate_user_price', models.IntegerField(default=7000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Category')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Publisher')),
            ],
        ),
    ]
