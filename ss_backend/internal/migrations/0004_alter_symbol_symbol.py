# Generated by Django 4.2.7 on 2023-11-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0003_alter_stockdata_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='symbol',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]