# Generated by Django 4.0.2 on 2022-04-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcherapp', '0002_vacancy_about_company_vacancy_level_english_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='years_in_work',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Intern'), (2, 'Junior'), (3, 'Middle'), (4, 'Senior')], default=1, null=True),
        ),
    ]
