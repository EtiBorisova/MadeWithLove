# Generated by Django 4.2.11 on 2024-04-15 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profilemodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='id',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
