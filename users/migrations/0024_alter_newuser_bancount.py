# Generated by Django 4.2 on 2023-06-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_newuser_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='bancount',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
