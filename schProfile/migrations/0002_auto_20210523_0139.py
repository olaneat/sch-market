# Generated by Django 3.1.3 on 2021-05-23 01:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('schProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
