# Generated by Django 2.0 on 2017-12-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20171207_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Quantity'),
        ),
    ]
