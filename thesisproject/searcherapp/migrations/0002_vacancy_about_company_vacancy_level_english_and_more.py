# Generated by Django 4.0.2 on 2022-04-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='about_company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='level_english',
            field=models.CharField(blank=True, choices=[('A1', 'Elementary'), ('A2', 'Pre-Intermediate'), ('B2', 'Upper-Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], default='A1', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='mail_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='site_company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='site_in_dou',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='year_in_school',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Intern'), (2, 'Junior'), (3, 'Middle'), (4, 'Senior')], default=1, max_length=2, null=True),
        ),
    ]
