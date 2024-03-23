# Generated by Django 5.0.3 on 2024-03-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='reason_for_report',
            field=models.TextField(blank=True, null=True),
        ),
    ]
