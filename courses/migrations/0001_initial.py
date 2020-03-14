# Generated by Django 3.0.3 on 2020-03-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('organizer', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('course_src', models.URLField()),
                ('picture_src', models.URLField(blank=True, null=True)),
                ('date_posted', models.DateField()),
                ('skills_taught', models.ManyToManyField(to='skills.Skill')),
            ],
        ),
    ]