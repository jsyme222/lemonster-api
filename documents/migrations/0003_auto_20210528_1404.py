# Generated by Django 3.2.2 on 2021-05-28 14:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20210528_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='doc_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.documenttype'),
        ),
        migrations.AddField(
            model_name='privatedocument',
            name='doc_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.documenttype'),
        ),
    ]