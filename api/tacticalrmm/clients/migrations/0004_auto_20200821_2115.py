# Generated by Django 3.1 on 2020-08-21 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_auto_20200617_0332'),
        ('clients', '0003_auto_20200609_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='policy',
        ),
        migrations.RemoveField(
            model_name='site',
            name='policy',
        ),
        migrations.AddField(
            model_name='client',
            name='server_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='server_clients', to='automation.policy'),
        ),
        migrations.AddField(
            model_name='client',
            name='workstation_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workstation_clients', to='automation.policy'),
        ),
        migrations.AddField(
            model_name='site',
            name='server_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='server_sites', to='automation.policy'),
        ),
        migrations.AddField(
            model_name='site',
            name='workstation_policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workstation_sites', to='automation.policy'),
        ),
    ]
