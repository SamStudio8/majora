# Generated by Django 2.2.10 on 2020-03-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0016_biosampleartifact_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biosamplesource',
            name='source_age',
        ),
        migrations.AddField(
            model_name='biosourcesamplingprocess',
            name='source_age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
