# Generated by Django 2.2.6 on 2019-11-04 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='flat_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signin.UserProfile'),
        ),
    ]
