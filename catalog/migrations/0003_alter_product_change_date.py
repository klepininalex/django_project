# Generated by Django 4.2.4 on 2023-08-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='дата создания'),
        ),
    ]