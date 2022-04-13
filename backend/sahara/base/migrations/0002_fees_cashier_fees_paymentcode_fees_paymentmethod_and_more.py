# Generated by Django 4.0.1 on 2022-04-12 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='cashier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.supportstaff'),
        ),
        migrations.AddField(
            model_name='fees',
            name='paymentCode',
            field=models.CharField(default='-', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fees',
            name='paymentMethod',
            field=models.CharField(choices=[('MOBILE', 'MOBILE'), ('CHEQUE', 'CHEQUE'), ('CASH', 'CASH')], default='CHEQUE', max_length=20),
        ),
        migrations.AddField(
            model_name='fees',
            name='paymentTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
