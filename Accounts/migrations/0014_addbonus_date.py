# Generated by Django 3.2.7 on 2021-09-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0013_addbonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbonus',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
