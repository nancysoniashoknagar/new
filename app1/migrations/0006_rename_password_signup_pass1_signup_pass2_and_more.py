# Generated by Django 4.1.5 on 2023-01-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='password',
            new_name='pass1',
        ),
        migrations.AddField(
            model_name='signup',
            name='pass2',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='uname',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
