# Generated by Django 4.2.2 on 2023-06-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('salary', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]