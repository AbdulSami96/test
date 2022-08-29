# Generated by Django 4.0.5 on 2022-07-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chocolate_name', models.CharField(max_length=100)),
                ('chocolate_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Dairyproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dairyproduct_name', models.CharField(max_length=100)),
                ('dairyproduct_price', models.FloatField()),
            ],
        ),
    ]
