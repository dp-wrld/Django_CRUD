# Generated by Django 4.0.6 on 2022-07-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]