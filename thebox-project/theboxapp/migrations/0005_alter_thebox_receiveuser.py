# Generated by Django 4.1.3 on 2022-11-26 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theboxapp', '0004_remove_donatedmealswipe_donatedby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thebox',
            name='receiveUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
