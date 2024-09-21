# Generated by Django 4.2.14 on 2024-08-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoltMan', '0003_alter_bolt_geometry_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washer',
            name='idiameter',
            field=models.FloatField(default=0, verbose_name='Inside Diameter (mm)'),
        ),
        migrations.AlterField(
            model_name='washer',
            name='odiameter',
            field=models.FloatField(default=0, verbose_name='Outside Diameter (mm)'),
        ),
        migrations.AlterField(
            model_name='washer',
            name='thickness',
            field=models.FloatField(default=0, verbose_name='Thickness (mm)'),
        ),
    ]
