# Generated by Django 3.1.7 on 2021-04-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='bed_name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]