# Generated by Django 4.2.7 on 2023-11-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_discount_user_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
