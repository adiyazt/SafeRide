# Generated by Django 5.0.1 on 2024-02-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxist',
            name='geoposition',
            field=models.CharField(default='49.8000567 73.0895435', max_length=120, verbose_name='Локация'),
        ),
        migrations.AddField(
            model_name='taxist',
            name='is_free',
            field=models.BooleanField(default=True, verbose_name='Свободен?'),
        ),
    ]