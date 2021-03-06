# Generated by Django 2.1.3 on 2018-11-03 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0002_auto_20181102_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrega.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destinatario', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=50)),
                ('ciudad', models.ManyToManyField(through='entrega.Asignacion', to='entrega.Ciudad')),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrega.Piloto')),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='paquete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrega.Paquete'),
        ),
    ]
