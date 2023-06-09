# Generated by Django 4.2 on 2023-05-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('path', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamifiedCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descreption', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('points', models.IntegerField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
