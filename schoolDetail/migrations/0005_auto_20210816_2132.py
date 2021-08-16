# Generated by Django 3.1.3 on 2021-08-16 21:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schoolDetail', '0004_remove_review_reviewer_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
