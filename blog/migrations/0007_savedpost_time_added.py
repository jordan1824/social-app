# Generated by Django 3.0.8 on 2020-08-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_savedpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedpost',
            name='time_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
