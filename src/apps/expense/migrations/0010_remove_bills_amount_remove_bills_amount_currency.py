# Generated by Django 4.2.6 on 2023-11-28 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0009_alter_billsaccount_user_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bills',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='bills',
            name='amount_currency',
        ),
    ]
