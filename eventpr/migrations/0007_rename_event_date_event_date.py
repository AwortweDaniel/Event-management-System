# Generated by Django 5.1.4 on 2024-12-23 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventpr', '0006_remove_registration_event_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='date',
        ),
    ]
