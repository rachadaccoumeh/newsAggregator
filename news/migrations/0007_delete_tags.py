# Generated by Django 4.1.5 on 2023-02-03 16:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0006_tags"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tags",
        ),
    ]
