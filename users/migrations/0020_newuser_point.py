# Generated by Django 4.2 on 2023-05-26 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_newuser_bancount'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='point',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
