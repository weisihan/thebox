# Generated by Django 4.1.2 on 2022-11-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theboxapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donatedmealswipe',
            name='receivedBy',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='donatedmealswipe',
            name='receivedTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
