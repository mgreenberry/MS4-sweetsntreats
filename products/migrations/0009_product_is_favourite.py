# Generated by Django 3.2 on 2022-03-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220224_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
