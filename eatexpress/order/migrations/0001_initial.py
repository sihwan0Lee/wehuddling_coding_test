# Generated by Django 3.0.5 on 2021-02-16 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(default='0', verbose_name='총 가격')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='주문 날짜')),
                ('status', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=8, verbose_name='주문상태')),
            ],
            options={
                'verbose_name': '주문 장바구니',
                'verbose_name_plural': '주문 장바구니',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='주문갯수')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': '주문 상품',
                'verbose_name_plural': '주문 상품',
                'db_table': 'order_products',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='order.OrderProduct', to='product.Product', verbose_name='상품명'),
        ),
    ]
