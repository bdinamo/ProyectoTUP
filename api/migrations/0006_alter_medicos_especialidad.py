# Generated by Django 4.0.4 on 2022-05-14 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_medicos_especialidad_medicos_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.especialidad'),
        ),
    ]
