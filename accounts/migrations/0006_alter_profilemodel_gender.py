# Generated by Django 4.2.11 on 2024-04-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profilemodel_id_profilemodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'MALE'), ('FEMALE', 'Female'), ('DO NOT SHOW', 'Do not show')], max_length=30, null=True),
        ),
    ]