# Generated by Django 2.1.5 on 2019-02-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190204_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
