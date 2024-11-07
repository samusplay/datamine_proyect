# Generated by Django 5.1.2 on 2024-11-07 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0003_alter_factura_contador_mes_anterior_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='consumo_kwh_por_hora',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='factura',
            name='costo_total_cop',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
