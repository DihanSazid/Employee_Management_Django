# Generated by Django 3.2.7 on 2021-09-14 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_remove_sale_total_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='employee',
            new_name='employee_name',
        ),
    ]