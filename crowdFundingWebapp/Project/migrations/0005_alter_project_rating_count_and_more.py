# Generated by Django 5.0.3 on 2024-03-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_project_rating_count_project_total_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='rating_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_rating',
            field=models.IntegerField(default=0),
        ),
    ]