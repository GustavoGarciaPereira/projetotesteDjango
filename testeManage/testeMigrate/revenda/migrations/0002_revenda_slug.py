# Generated by Django 2.1.3 on 2018-11-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenda',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]