# Generated by Django 5.1.3 on 2024-11-22 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("logg", "0007_token"),
    ]

    operations = [
        migrations.RenameField(
            model_name="token",
            old_name="username",
            new_name="user",
        ),
    ]
