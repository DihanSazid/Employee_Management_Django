# Generated by Django 3.2.7 on 2021-09-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_sale_total_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_sale',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
