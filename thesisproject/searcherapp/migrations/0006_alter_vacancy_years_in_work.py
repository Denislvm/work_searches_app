# Generated by Django 4.0.2 on 2022-04-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcherapp', '0005_alter_vacancy_level_english'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='years_in_work',
            field=models.CharField(blank=True, choices=[('Intern', 'Intern'), ('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default='Junior', max_length=50, null=True),
        ),
    ]
