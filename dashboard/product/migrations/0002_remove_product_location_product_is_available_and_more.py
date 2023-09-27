# Generated by Django 4.2.5 on 2023-09-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='location',
        ),
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]