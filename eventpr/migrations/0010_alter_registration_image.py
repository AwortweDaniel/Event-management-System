# Generated by Django 5.1.4 on 2024-12-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpr', '0009_registration_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='image',
            field=models.ImageField(default='pic/37.jpg', editable=False, upload_to='pic'),
        ),
    ]