# Generated by Django 4.2 on 2023-05-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_challenges_end_date_challenges_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='descreption',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]