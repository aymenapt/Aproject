# Generated by Django 4.2 on 2023-06-05 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('path', '0005_remove_gamifiedcours_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningpath',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='learningpath', to=settings.AUTH_USER_MODEL),
        ),
    ]