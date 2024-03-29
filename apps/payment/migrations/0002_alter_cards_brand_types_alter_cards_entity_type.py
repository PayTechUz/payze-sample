# Generated by Django 4.2.5 on 2024-01-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='brand_types',
            field=models.CharField(blank=True, choices=[(1, 'UZCARD'), (2, 'HUMO'), (3, 'MASTERCARD'), (4, 'VISA')], max_length=100, null=True, verbose_name='Brand Types'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='entity_type',
            field=models.CharField(choices=[(1, 'PRIVATE'), (2, 'CORPORATE'), (3, 'UNKNOWN')], max_length=100, verbose_name='Entity Type'),
        ),
    ]
