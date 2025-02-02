# Generated by Django 4.2.10 on 2024-05-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatiaFramework', '0076_remove_workflow_action_is_for_all_instances'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow_action',
            name='is_for_all_instances',
            field=models.BooleanField(default=False, verbose_name='Execute on all required instances'),
        ),
    ]
