# Generated by Django 4.0.4 on 2022-10-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=10, null=True),
        ),
    ]