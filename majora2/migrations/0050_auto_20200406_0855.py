# Generated by Django 2.2.10 on 2020-04-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0049_auto_20200406_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majoraartifactgroup',
            name='dice_name',
            field=models.CharField(blank=True, max_length=96, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='majoraartifactgroup',
            name='meta_name',
            field=models.CharField(blank=True, max_length=96, null=True),
        ),
    ]
