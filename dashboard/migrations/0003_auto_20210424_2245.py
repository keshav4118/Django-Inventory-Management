# Generated by Django 3.1.6 on 2021-04-24 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Prodects'},
        ),
    ]