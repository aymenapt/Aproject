# Generated by Django 4.2 on 2023-04-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_name_newuser_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='role',
            field=models.CharField(default='admin', max_length=40),
        ),
    ]
