# Generated by Django 3.2.14 on 2022-07-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_categories_price_remove_categories_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]