# Generated by Django 4.1.5 on 2023-01-22 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_rename_email_signup_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
