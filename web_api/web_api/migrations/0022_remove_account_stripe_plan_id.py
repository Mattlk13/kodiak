# Generated by Django 3.0.3 on 2020-06-17 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web_api", "0021_auto_20200617_1246"),
    ]

    operations = [
        migrations.RemoveField(model_name="account", name="stripe_plan_id",),
    ]