# Generated by Django 3.2.2 on 2021-06-02 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210602_0754'),
        ('projects', '0001_initial'),
        ('tags', '0003_alter_blogtag_usage_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogTag',
        ),
    ]