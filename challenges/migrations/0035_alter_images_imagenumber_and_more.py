# Generated by Django 4.2 on 2023-06-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0034_alter_challenges_max_teamsize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='imagenumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='paragraphnumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participate',
            name='participate_result',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_point',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='taskfile',
            name='filenumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='titel',
            name='titelnumber',
            field=models.IntegerField(default=0),
        ),
    ]
