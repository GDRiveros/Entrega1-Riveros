# Generated by Django 4.1.1 on 2022-10-11 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Biblioteca", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Clientes",
            new_name="Cliente",
        ),
        migrations.RenameModel(
            old_name="Empleados",
            new_name="Empleado",
        ),
        migrations.RenameModel(
            old_name="Libros",
            new_name="Libro",
        ),
    ]
