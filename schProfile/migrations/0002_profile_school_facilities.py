# Generated by Django 3.1.3 on 2021-05-20 00:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='school_facilities',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
