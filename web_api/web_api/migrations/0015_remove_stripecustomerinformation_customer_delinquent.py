# Generated by Django 3.0.3 on 2020-03-24 03:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web_api", "0014_auto_20200323_0159"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stripecustomerinformation",
            name="customer_delinquent",
        ),
    ]
