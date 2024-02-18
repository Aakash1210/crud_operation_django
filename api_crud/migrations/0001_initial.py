# Generated by Django 4.2.10 on 2024-02-18 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('physical_address', models.CharField(max_length=255)),
                ('virtual_address', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
                ('network_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_crud.networkadmin')),
            ],
        ),
    ]