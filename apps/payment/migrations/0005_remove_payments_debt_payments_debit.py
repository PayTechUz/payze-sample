# Generated by Django 4.2.5 on 2024-01-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payments_credit_alter_payments_debt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='debt',
        ),
        migrations.AddField(
            model_name='payments',
            name='debit',
            field=models.FloatField(default=0, null=True, verbose_name='Debit'),
        ),
    ]