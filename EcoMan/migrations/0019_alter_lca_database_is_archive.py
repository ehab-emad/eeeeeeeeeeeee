# Generated by Django 4.2.7 on 2024-01-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoMan', '0018_alter_lca_database_is_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lca_database',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='Archived (not selectable)'),
        ),
    ]
