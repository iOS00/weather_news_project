# Generated by Django 3.2.3 on 2023-05-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]