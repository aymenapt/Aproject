# Generated by Django 4.2 on 2023-04-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_newuser_baned_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='bancount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
