# Generated by Django 4.0.4 on 2022-05-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_medicos_especialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicos',
            name='especialidad',
        ),
        migrations.AddField(
            model_name='medicos',
            name='especialidad',
            field=models.ManyToManyField(to='api.especialidad'),
        ),
    ]
