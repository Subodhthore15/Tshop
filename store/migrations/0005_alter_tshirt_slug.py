# Generated by Django 3.2.6 on 2021-09-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_tshirt_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='slug',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
