# Generated by Django 3.2.4 on 2021-06-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
