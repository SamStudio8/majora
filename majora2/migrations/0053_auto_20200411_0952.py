# Generated by Django 2.2.10 on 2020-04-11 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0052_pipehook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorametarecord',
            name='artifact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='majora2.MajoraArtifact'),
        ),
        migrations.AlterField(
            model_name='majorametarecord',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='majora2.MajoraArtifactGroup'),
        ),
        migrations.AlterField(
            model_name='majorametarecord',
            name='pgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='majora2.MajoraArtifactProcessGroup'),
        ),
        migrations.AlterField(
            model_name='majorametarecord',
            name='process',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='majora2.MajoraArtifactProcess'),
        ),
    ]
