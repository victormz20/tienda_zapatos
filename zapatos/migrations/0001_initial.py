# Generated by Django 5.0.3 on 2024-03-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zapato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('proveedor', models.CharField(max_length=200)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]