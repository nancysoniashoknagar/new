# Generated by Django 4.1.5 on 2023-01-21 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_password1_signup_pass1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='email',
            new_name='pass1',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='password',
            new_name='username',
        ),
    ]
