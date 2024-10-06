# Generated by Django 4.2.16 on 2024-10-05 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0047_alter_coresettings_notify_on_warning_alerts"),
        ("agents", "0059_alter_agenthistory_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="agenthistory",
            name="collector_all_output",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="agenthistory",
            name="custom_field",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="history",
                to="core.customfield",
            ),
        ),
        migrations.AddField(
            model_name="agenthistory",
            name="save_to_agent_note",
            field=models.BooleanField(default=False),
        ),
    ]
