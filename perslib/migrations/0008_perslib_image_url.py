# Generated by Django 5.0.6 on 2024-07-09 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perslib', '0007_remove_login_username_login_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='perslib',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
