# Generated by Django 4.2.2 on 2023-09-09 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_users_biblioteca_activo_alter_biblioteca_des_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biblioteca',
            name='activo',
        ),
    ]
