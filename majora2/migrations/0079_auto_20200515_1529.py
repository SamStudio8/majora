# Generated by Django 2.2.10 on 2020-05-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0078_auto_20200513_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishedartifactgroup',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
