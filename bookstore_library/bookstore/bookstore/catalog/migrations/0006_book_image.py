# Generated by Django 2.0 on 2017-12-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=None, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
