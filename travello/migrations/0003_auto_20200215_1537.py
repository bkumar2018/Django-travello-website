# Generated by Django 2.1.15 on 2020-02-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20200215_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(),
        ),
    ]
