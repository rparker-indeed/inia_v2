# Generated by Django 2.2 on 2019-06-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inia', '0012_savedsearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iniagene',
            name='gene_symbol',
            field=models.CharField(blank=True, db_index=True, max_length=255),
        ),
    ]