# Generated by Django 2.2.10 on 2020-07-16 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0106_profileagreementdefinition_is_terminable'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajoraDataview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MajoraDataviewSerializerField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=64)),
                ('model_field', models.CharField(max_length=64)),
                ('dataview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='majora2.MajoraDataview')),
            ],
        ),
    ]
