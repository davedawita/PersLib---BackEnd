# Generated by Django 5.0.6 on 2024-06-30 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perslib', '0002_alter_userprofile_managers_userprofile_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
