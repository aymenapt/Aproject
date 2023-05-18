# Generated by Django 4.2 on 2023-05-14 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0009_remove_challenges_format_challengerules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registre', to='challenges.challenges')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registre', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]