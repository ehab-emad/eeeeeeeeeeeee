# Generated by Django 4.2.7 on 2024-01-19 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CatiaFramework', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dotnet_module',
            old_name='parent_group',
            new_name='parent_module',
        ),
    ]
