# Generated by Django 4.2.5 on 2023-09-21 14:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("escola", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="atividades",
            old_name="atividate",
            new_name="atividade",
        ),
    ]
