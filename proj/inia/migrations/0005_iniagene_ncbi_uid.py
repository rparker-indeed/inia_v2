# Generated by Django 2.1.5 on 2019-01-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inia', '0004_auto_20190129_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='iniagene',
            name='ncbi_uid',
            field=models.IntegerField(default=None, null=True),
        ),
    ]