# Generated by Django 2.2 on 2019-05-07 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logininfo',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]