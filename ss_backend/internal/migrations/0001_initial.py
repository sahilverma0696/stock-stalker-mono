# Generated by Django 4.2.6 on 2023-10-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
                ('symbol', models.CharField(max_length=255)),
            ],
            options={
                'unique_together': {('date', 'symbol')},
            },
        ),
    ]
