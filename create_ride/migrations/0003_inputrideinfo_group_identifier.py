# Generated by Django 2.2 on 2019-05-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_ride', '0002_inputrideinfo_ride_status_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputrideinfo',
            name='group_identifier',
            field=models.IntegerField(default=1),
        ),
    ]