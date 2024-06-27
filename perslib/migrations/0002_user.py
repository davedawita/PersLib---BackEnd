# Generated by Django 5.0.6 on 2024-06-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perslib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]