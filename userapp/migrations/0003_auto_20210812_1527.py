# Generated by Django 3.1.7 on 2021-08-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20210812_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_compdetails',
            name='jobldate',
            field=models.IntegerField(null=True),
        ),
    ]