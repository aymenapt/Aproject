# Generated by Django 4.2 on 2023-05-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0006_challenges_is_planified'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='format',
            field=models.CharField(default='Jeopardy', max_length=255),
        ),
        migrations.AddField(
            model_name='challenges',
            name='max_teamsize',
            field=models.IntegerField(default=0),
        ),
    ]
