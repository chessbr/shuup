# Generated by Django 2.2.17 on 2021-01-23 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0081_package_link_related_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopproduct',
            options={'verbose_name': 'shop product', 'verbose_name_plural': 'shop products'},
        ),
    ]