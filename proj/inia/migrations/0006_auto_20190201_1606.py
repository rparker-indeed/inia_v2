# Generated by Django 2.1.5 on 2019-02-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inia', '0005_iniagene_ncbi_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brainregion',
            name='is_super_group',
        ),
        migrations.RemoveField(
            model_name='brainregion',
            name='sub_groups',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='brain_region',
        ),
        migrations.AddField(
            model_name='dataset',
            name='brain_region',
            field=models.ManyToManyField(to='inia.BrainRegion'),
        ),
    ]
