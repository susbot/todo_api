# Generated by Django 3.1.14 on 2022-05-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='body',
            field=models.TextField(default='you idiot'),
            preserve_default=False,
        ),
    ]
