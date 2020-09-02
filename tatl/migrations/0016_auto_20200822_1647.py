# Generated by Django 2.2.13 on 2020-08-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatl', '0015_auto_20200822_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='tatlpagerequest',
            name='response_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tatlpagerequest',
            name='status_code',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]