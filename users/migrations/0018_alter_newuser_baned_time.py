# Generated by Django 4.2 on 2023-04-29 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_newuser_baned_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='baned_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
