# Generated by Django 3.1.6 on 2021-02-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20210206_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default='0', verbose_name='총 가격'),
        ),
    ]