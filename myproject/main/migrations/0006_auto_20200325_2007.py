# Generated by Django 3.0.4 on 2020-03-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200325_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
