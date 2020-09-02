# Generated by Django 2.2.13 on 2020-08-22 17:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tatl', '0020_delete_tatlpagerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tatlrequest',
            name='response_uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True),
        ),
    ]