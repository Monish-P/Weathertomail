# Generated by Django 3.2.6 on 2022-01-11 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
