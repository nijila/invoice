# Generated by Django 2.2.13 on 2020-08-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
