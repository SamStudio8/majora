# Generated by Django 2.2.10 on 2020-03-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0032_auto_20200325_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorametarecord',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='majorametarecord',
            name='value',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
