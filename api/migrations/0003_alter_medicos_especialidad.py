# Generated by Django 4.0.4 on 2022-05-14 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_medicos_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='especialidades', to='api.especialidad'),
        ),
    ]
