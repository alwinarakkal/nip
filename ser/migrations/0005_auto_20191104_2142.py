# Generated by Django 2.2.6 on 2019-11-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0004_auto_20191104_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='flat_number',
            field=models.CharField(max_length=30),
        ),
    ]
