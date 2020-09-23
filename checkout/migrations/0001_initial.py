# Generated by Django 3.1.1 on 2020-09-23 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(editable=False, max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('emailaddress', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=80)),
                ('address2', models.CharField(blank=True, max_length=80, null=True)),
                ('town', models.CharField(max_length=40)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(max_length=40)),
                ('orderdate', models.DateTimeField(auto_now_add=True)),
                ('delivery', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('finaltotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SingleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('singleordertotal', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singleorder', to='checkout.userorders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
