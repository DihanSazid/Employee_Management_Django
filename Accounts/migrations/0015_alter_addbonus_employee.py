# Generated by Django 3.2.7 on 2021-09-14 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0014_addbonus_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbonus',
            name='employee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]