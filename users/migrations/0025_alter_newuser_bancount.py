# Generated by Django 4.2 on 2023-06-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_newuser_bancount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='bancount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
