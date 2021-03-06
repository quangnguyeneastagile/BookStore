# Generated by Django 2.0 on 2017-12-12 06:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book author', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter book title', max_length=200)),
                ('description', models.TextField(default='No description availalbe.')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('image', models.ImageField(default=None, upload_to='uploads/%Y/%m/%d/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book category', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(help_text='Enter user ID', max_length=200)),
                ('email', models.CharField(help_text='Enter email', max_length=200)),
                ('password', models.CharField(help_text='Enter password', max_length=200)),
                ('phone', models.CharField(help_text='Enter phone number', max_length=200)),
                ('full_name', models.CharField(help_text='Enter full name', max_length=200)),
                ('birthday', models.DateField(blank=True, help_text='Enter birthday', null=True)),
                ('account_created_date', models.DateField(default=datetime.datetime.today)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category'),
        ),
    ]
