# Generated by Django 3.1 on 2020-08-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newsania', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
