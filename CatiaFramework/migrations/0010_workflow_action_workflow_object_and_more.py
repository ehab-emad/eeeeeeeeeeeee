# Generated by Django 4.2.7 on 2024-01-28 13:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('NormMan', '0003_alter_workflow_session_created_objects'),
        ('CatiaFramework', '0009_remove_dotnet_component_content_summary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workflow_Action',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=False, verbose_name='Job will be visible for other colleagues within the same project')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
                ('framework_request', models.UUIDField(blank=True, null=True, verbose_name='Framework Request UUID')),
                ('is_active', models.BooleanField(default=False, verbose_name='')),
                ('is_automatic', models.BooleanField(default=False, verbose_name='Action will be called automatically')),
                ('automatic_trigger', models.UUIDField(default=uuid.uuid4, verbose_name='Tigger Action UUID')),
                ('comment_section', models.CharField(blank=True, max_length=100000, null=True)),
                ('content_section', models.CharField(blank=True, max_length=3000000, null=True)),
                ('summary_section', models.CharField(blank=True, max_length=10000, null=True)),
                ('access_modifier', models.CharField(choices=[('NONE', 'None')], default='NONE', max_length=50)),
                ('type', models.CharField(choices=[('NONE', 'None')], default='NONE', max_length=50)),
                ('accessibility', models.CharField(choices=[('PRIVATE', 'Private'), ('DATABASE_USERS', 'Database Users'), ('PROJECT_USERS', 'Project Users')], default='private', max_length=50)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('IS_DONE', 'Done'), ('FAILED', 'Failed'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=50)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CatiaFramework.projectuser_catiaframework_ref')),
                ('project_model', models.ForeignKey(blank=True, default=None, help_text='Select a a project for Shared Component', on_delete=django.db.models.deletion.CASCADE, to='CatiaFramework.project_catiaframework_ref', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow_Object',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=False, verbose_name='Job will be visible for other colleagues within the same project')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
                ('type', models.CharField(choices=[('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=50)),
                ('accessibility', models.CharField(choices=[('PRIVATE', 'Private'), ('DATABASE_USERS', 'Database Users'), ('PROJECT_USERS', 'Project Users')], default='private', max_length=50)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('IS_DONE', 'Done'), ('FAILED', 'Failed'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=50)),
                ('actions', models.ManyToManyField(blank=True, to='CatiaFramework.workflow_action', verbose_name='Actions')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CatiaFramework.projectuser_catiaframework_ref')),
            ],
        ),
        migrations.AlterField(
            model_name='dotnet_component',
            name='type',
            field=models.CharField(choices=[('VBDOTNET_CLASS', 'vb.net class'), ('VBDOTNET_MODULE', 'vb.net module'), ('VBDOTNET_SUB', 'vb.net sub procedure'), ('VBDOTNET_FUNCTION', 'vb.net function'), ('VBDOTNET_PROPERTY', 'vb.net property'), ('DJANGO_VIEW', 'Django view'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=50),
        ),
        migrations.CreateModel(
            name='Workflow_Stage',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('IS_DONE', 'Done'), ('FAILED', 'Failed'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=50)),
                ('is_active', models.BooleanField(default=False, verbose_name='')),
                ('type', models.CharField(choices=[('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=50)),
                ('actions', models.ManyToManyField(blank=True, to='CatiaFramework.workflow_action', verbose_name='Actions')),
                ('objects', models.ManyToManyField(blank=True, to='CatiaFramework.workflow_object', verbose_name='Created Objects')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CatiaFramework.projectuser_catiaframework_ref')),
                ('parent_stage', models.ForeignKey(blank=True, default=None, help_text='Parent Dependent Session', on_delete=django.db.models.deletion.CASCADE, to='CatiaFramework.workflow_stage', verbose_name='Parent Stage')),
                ('project_model', models.ForeignKey(blank=True, default=None, help_text='Select a a project for Shared Component', on_delete=django.db.models.deletion.CASCADE, to='CatiaFramework.project_catiaframework_ref', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=False, verbose_name='Job will be visible for other colleagues within the same project')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
                ('gif', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Part Image')),
                ('version', models.IntegerField(blank=True, default=0, editable=False, null=True)),
                ('type', models.CharField(choices=[('USER_SESSION', 'User Session'), ('DATABASE_TEMPLATE', 'Database Template'), ('FRAMEWORK_INTERNAL', 'Framework Internal')], default='DATABASE_TEMPLATE', max_length=50)),
                ('accessibility', models.CharField(choices=[('PRIVATE', 'Private'), ('DATABASE_USERS', 'Database Users'), ('PROJECT_USERS', 'Project Users')], default='private', max_length=50)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('IS_DONE', 'Done'), ('FAILED', 'Failed'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=50)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CatiaFramework.projectuser_catiaframework_ref')),
                ('project_model', models.ForeignKey(blank=True, default=None, help_text='Select a a project for Shared Component', on_delete=django.db.models.deletion.CASCADE, to='CatiaFramework.project_catiaframework_ref', verbose_name='Project')),
                ('shared_component', models.ForeignKey(blank=True, default=None, help_text='Select a a project for Shared Component', on_delete=django.db.models.deletion.CASCADE, to='NormMan.normparts_shared_component', verbose_name='Project')),
                ('stages', models.ManyToManyField(blank=True, to='CatiaFramework.workflow_stage', verbose_name='Workflow Stage')),
            ],
        ),
    ]
