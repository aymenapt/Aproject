# Generated by Django 4.2 on 2023-04-29 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_newuser_bancount'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='baned_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
