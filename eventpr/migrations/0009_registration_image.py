# Generated by Django 5.1.4 on 2024-12-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpr', '0008_registration_dateevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='image',
            field=models.ImageField(default='../pic/37.jpg', editable=False, upload_to='pic'),
        ),
    ]
