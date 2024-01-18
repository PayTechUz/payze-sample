# Generated by Django 4.2.5 on 2024-01-18 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_cardverifypayment_final_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=30, verbose_name='Full Name')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Phone Number')),
            ],
            options={
                'db_table': 'card_payer',
            },
        ),
        migrations.AddField(
            model_name='cards',
            name='payer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.payer', verbose_name='Payer'),
        ),
    ]
