# Generated by Django 2.1.5 on 2019-02-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inia', '0009_auto_20190207_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homologene',
            name='ncbi_uid',
            field=models.IntegerField(db_index=True, unique=True),
        ),
    ]
