# Generated by Django 2.2.13 on 2020-10-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0128_auto_20201017_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='coguk_biosourcesamplingprocesssupplement',
            name='collection_pillar',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
