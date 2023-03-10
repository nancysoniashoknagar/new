# Generated by Django 4.1.5 on 2023-01-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('fname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('dob', models.CharField(max_length=15)),
                ('mob', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('fname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('dob', models.CharField(max_length=15)),
                ('mob', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('fname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('dob', models.CharField(max_length=15)),
                ('mob', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
