# Generated by Django 5.1.4 on 2024-12-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpr', '0011_remove_registration_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='image',
            field=models.ImageField(default='37.jpg', editable=False, upload_to='pic'),
        ),
    ]
