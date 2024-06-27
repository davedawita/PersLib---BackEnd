# Generated by Django 5.0.6 on 2024-06-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perslib', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
            ],
        ),
    ]