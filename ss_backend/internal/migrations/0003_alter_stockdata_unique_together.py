# Generated by Django 4.2.7 on 2023-11-13 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stockdata',
            unique_together={('date', 'symbol')},
        ),
    ]