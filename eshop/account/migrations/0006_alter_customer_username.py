# Generated by Django 4.1.2 on 2022-10-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=155, null=True, unique=True),
        ),
    ]
