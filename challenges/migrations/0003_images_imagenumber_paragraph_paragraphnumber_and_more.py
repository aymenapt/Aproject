# Generated by Django 4.2 on 2023-05-02 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_alter_challenges_image_alter_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='imagenumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='paragraphnumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='titel',
            name='titelnumber',
            field=models.IntegerField(default=0),
        ),
    ]
