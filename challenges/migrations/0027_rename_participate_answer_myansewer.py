# Generated by Django 4.2 on 2023-06-03 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0026_answer_participate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='participate',
            new_name='myansewer',
        ),
    ]
