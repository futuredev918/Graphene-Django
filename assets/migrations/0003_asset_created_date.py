# Generated by Django 2.2 on 2020-01-22 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20200120_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
