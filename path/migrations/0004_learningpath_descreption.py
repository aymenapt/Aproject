# Generated by Django 4.2 on 2023-05-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('path', '0003_gamifiedcours_learningpath'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningpath',
            name='descreption',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]