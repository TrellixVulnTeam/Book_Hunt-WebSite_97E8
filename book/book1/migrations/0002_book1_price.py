# Generated by Django 3.0.8 on 2020-07-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book1',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]