# Generated by Django 5.0.6 on 2024-06-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
