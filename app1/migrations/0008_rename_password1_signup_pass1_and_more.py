# Generated by Django 4.1.5 on 2023-01-21 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_rename_pass1_signup_password1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='password1',
            new_name='pass1',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='password2',
            new_name='pass2',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='username',
            new_name='uname',
        ),
    ]
