# Generated by Django 3.2.14 on 2022-07-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_products_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='des',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
