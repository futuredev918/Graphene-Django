# Generated by Django 2.2 on 2020-01-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0005_asset_firmwaredetail_firmwarecomponentdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='ovid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
