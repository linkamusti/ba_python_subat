# Generated by Django 3.2.3 on 2021-05-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='title', max_length=20),
        ),
    ]
