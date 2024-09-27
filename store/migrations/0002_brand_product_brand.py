# Generated by Django 5.0.1 on 2024-04-28 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='media/images/products')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=int, on_delete=django.db.models.deletion.CASCADE, to='store.brand'),
            preserve_default=False,
        ),
    ]
