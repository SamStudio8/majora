# Generated by Django 2.2.10 on 2020-03-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0038_auto_20200327_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='biosourcesamplingprocess',
            name='received_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
