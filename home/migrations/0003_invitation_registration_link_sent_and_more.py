# Generated by Django 5.0.7 on 2024-08-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_users_email_verified"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitation",
            name="registration_link_sent",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="invitation",
            name="registration_token_expiry",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
