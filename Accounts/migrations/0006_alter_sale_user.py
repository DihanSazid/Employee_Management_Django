# Generated by Django 3.2.7 on 2021-09-14 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_alter_sale_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sale', to=settings.AUTH_USER_MODEL),
        ),
    ]
