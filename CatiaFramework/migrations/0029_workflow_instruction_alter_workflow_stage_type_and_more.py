# Generated by Django 4.2.7 on 2024-01-30 06:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CatiaFramework', '0028_alter_workflow_action_automatic_trigger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workflow_Instruction',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
            ],
        ),
        migrations.AlterField(
            model_name='workflow_stage',
            name='type',
            field=models.CharField(choices=[('UNDEFINED', 'Undefined'), ('PROCESS', 'Process'), ('WORKFLOW', 'Workflow'), ('STEP', 'Step')], default='UNDEFINED', max_length=50),
        ),
        migrations.AddField(
            model_name='workflow',
            name='instruction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CatiaFramework.workflow_instruction', verbose_name='Instruction'),
        ),
        migrations.AddField(
            model_name='workflow_action',
            name='instruction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CatiaFramework.workflow_instruction', verbose_name='Instruction'),
        ),
        migrations.AddField(
            model_name='workflow_object',
            name='instruction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CatiaFramework.workflow_instruction', verbose_name='Instruction'),
        ),
        migrations.AddField(
            model_name='workflow_stage',
            name='instruction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CatiaFramework.workflow_instruction', verbose_name='Instruction'),
        ),
    ]
