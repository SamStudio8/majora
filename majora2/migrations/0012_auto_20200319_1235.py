# Generated by Django 2.2.10 on 2020-03-19 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0011_auto_20200319_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='biosourcesamplingprocess',
            name='collected_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biosourcesamplingprocess',
            name='collection_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collected_sample_records', to='majora2.Institute'),
        ),
        migrations.AlterField(
            model_name='biosourcesamplingprocess',
            name='submission_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submitted_sample_records', to='majora2.Institute'),
        ),
    ]
