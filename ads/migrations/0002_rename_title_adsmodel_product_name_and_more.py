# Generated by Django 4.2.11 on 2024-04-14 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adsmodel',
            old_name='title',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='adsmodel',
            old_name='user',
            new_name='seller',
        ),
    ]
