# Generated by Django 3.1.6 on 2022-11-30 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20210319_2344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='آدرس الکترونیکی'),
        ),
    ]