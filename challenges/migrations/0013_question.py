# Generated by Django 4.2 on 2023-05-19 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0012_taskfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=800)),
                ('question_number', models.IntegerField(default=0)),
                ('question_point', models.IntegerField()),
                ('question_solution', models.CharField(max_length=255)),
                ('question_hint', models.CharField(max_length=255)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='challenges.task')),
            ],
        ),
    ]
