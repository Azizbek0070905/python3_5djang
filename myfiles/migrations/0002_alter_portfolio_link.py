# Generated by Django 5.0.1 on 2024-01-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='link',
            field=models.CharField(max_length=40),
        ),
    ]
