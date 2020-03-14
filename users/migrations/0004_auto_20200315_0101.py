# Generated by Django 3.0.3 on 2020-03-14 17:01

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0002_auto_20200315_0056'),
        ('users', '0003_modifieduser_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='modifieduser',
            name='interests',
            field=models.ManyToManyField(to='interests.Interest'),
        ),
        migrations.AddField(
            model_name='modifieduser',
            name='location',
            field=django_countries.fields.CountryField(default=None, max_length=2),
        ),
    ]
