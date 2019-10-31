# Generated by Django 2.1.7 on 2019-04-01 19:13

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inia', '0011_auto_20190314_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_parameters', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]