# Generated by Django 5.0.1 on 2024-01-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0008_remove_subcribe_malumot_remove_subcribe_nomi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
