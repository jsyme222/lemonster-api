# Generated by Django 3.2.2 on 2021-07-04 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
        ('projects', '0002_auto_20210704_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcontentdocument',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.document'),
        ),
    ]
