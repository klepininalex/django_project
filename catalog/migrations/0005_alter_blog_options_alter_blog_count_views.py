# Generated by Django 4.2.4 on 2023-08-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='count_views',
            field=models.IntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]