# Generated by Django 2.2.13 on 2020-09-08 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0123_profileapppassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajoraDataviewFilterField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_field', models.CharField(max_length=64)),
                ('filter_type', models.CharField(choices=[('str', 'str'), ('int', 'int'), ('float', 'float'), ('bool', 'bool')], max_length=8)),
                ('filter_value', models.CharField(max_length=128)),
                ('filter_op', models.CharField(default='exact', max_length=10)),
                ('dataview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='majora2.MajoraDataview')),
            ],
        ),
    ]