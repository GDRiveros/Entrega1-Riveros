# Generated by Django 4.1.1 on 2022-10-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Biblioteca",
            "0002_rename_clientes_cliente_rename_empleados_empleado_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="edad",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="edad",
            field=models.IntegerField(null=True),
        ),
    ]
