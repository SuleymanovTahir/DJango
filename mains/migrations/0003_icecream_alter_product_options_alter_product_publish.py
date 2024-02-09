# Generated by Django 5.0.1 on 2024-01-27 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0002_alter_product_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Мороженное',
                'verbose_name_plural': 'Мороженное',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-name',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 15, 50, 21, 88893, tzinfo=datetime.timezone.utc)),
        ),
    ]
