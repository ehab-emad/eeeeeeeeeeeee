# Generated by Django 4.2.14 on 2024-08-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoltMan', '0010_bolted_part_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolted_part',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
    ]
