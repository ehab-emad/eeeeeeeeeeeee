# Generated by Django 4.2.7 on 2023-12-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoMan', '0014_alter_analysis_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='utilisation_instance_model',
            field=models.ManyToManyField(blank=True, to='EcoMan.utilisation_process', verbose_name='Utilisations processes'),
        ),
    ]
