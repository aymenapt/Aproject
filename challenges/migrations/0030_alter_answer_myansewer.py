# Generated by Django 4.2 on 2023-06-03 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0029_alter_answer_challenge_alter_answer_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='myansewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myanswer', to='challenges.participate'),
        ),
    ]
