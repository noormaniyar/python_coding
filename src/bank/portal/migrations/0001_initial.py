# Generated by Django 3.1.7 on 2021-04-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('pan_number', models.CharField(max_length=15)),
                ('account_number', models.CharField(max_length=15)),
                ('mobile_number', models.CharField(max_length=10)),
                ('balance', models.FloatField(default=0)),
            ],
        ),
    ]