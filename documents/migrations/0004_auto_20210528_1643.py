# Generated by Django 3.2.2 on 2021-05-28 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20210528_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.documenttype'),
        ),
        migrations.AlterField(
            model_name='document',
            name='notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='privatedocument',
            name='doc_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.documenttype'),
        ),
        migrations.AlterField(
            model_name='privatedocument',
            name='notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
