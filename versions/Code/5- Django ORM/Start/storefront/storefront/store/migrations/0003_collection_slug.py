# Generated by Django 5.0.4 on 2024-04-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_product_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='slug',
            field=models.SlugField(default='-'),
            preserve_default=False,
        ),
    ]
