# Generated by Django 3.2.2 on 2021-05-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_blogtag_usage_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtag',
            name='usage_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
