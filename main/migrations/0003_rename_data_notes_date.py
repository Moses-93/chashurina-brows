# Generated by Django 5.1.1 on 2024-09-16 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_service_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='data',
            new_name='date',
        ),
    ]
