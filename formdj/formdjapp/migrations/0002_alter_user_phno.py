# Generated by Django 4.1.1 on 2022-09-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formdjapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]