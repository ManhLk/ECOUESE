# Generated by Django 3.2.8 on 2021-10-21 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='activate',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='activate',
            new_name='active',
        ),
    ]
