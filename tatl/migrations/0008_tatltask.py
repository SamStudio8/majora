# Generated by Django 2.2.13 on 2020-08-07 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tatl', '0007_tatlrequest_response_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='TatlTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celery_uuid', models.UUIDField(unique=True)),
                ('task', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField()),
                ('response_time', models.DurationField(blank=True, null=True)),
                ('request', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task', to='tatl.TatlRequest')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
