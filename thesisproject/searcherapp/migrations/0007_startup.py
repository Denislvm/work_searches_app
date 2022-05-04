# Generated by Django 4.0.2 on 2022-05-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcherapp', '0006_alter_vacancy_years_in_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(verbose_name='About startup')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
