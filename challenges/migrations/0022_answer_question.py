# Generated by Django 4.2 on 2023-05-26 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0021_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='challenges.question'),
            preserve_default=False,
        ),
    ]
