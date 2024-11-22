# Generated by Django 5.1.3 on 2024-11-22 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logg", "0006_alter_user_managers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "username",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="logg.user"
                    ),
                ),
            ],
        ),
    ]
