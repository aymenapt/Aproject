# Generated by Django 4.2 on 2023-06-04 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_newuser_point'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newuser',
            options={'ordering': ('-point',)},
        ),
    ]
