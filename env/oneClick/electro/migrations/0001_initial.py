# Generated by Django 3.2.7 on 2022-01-10 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=11, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('profile_pic', models.FileField(blank=True, default='pizzriea.JPG', null=True, upload_to='profiles/')),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('otp', models.IntegerField(default=567)),
                ('view', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electro.registration')),
                ('product_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_order', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('ord_deliver_otp', models.IntegerField(default=7878)),
                ('order_notes', models.CharField(max_length=300, null=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='electro.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(default='1', max_length=100)),
                ('price', models.IntegerField(null=True)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electro.registration')),
                ('product_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('retailer_Id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.adminuser')),
            ],
        ),
    ]
