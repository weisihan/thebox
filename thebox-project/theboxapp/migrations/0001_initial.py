# Generated by Django 4.1.2 on 2022-11-23 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DonatedMealSwipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donatedBy', models.CharField(max_length=10)),
                ('receivedBy', models.CharField(max_length=10)),
                ('donatedTime', models.DateTimeField(auto_now_add=True)),
                ('receivedTime', models.DateTimeField(null=True)),
                ('availability', models.BooleanField(default=True)),
                ('donateUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]