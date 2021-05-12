# Generated by Django 3.2.2 on 2021-05-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactmail_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmail',
            name='company',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactmail',
            name='email',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactmail',
            name='name',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactmail',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contactmail',
            name='services_business_application',
            field=models.BooleanField(default=False, verbose_name='Application Services'),
        ),
        migrations.AlterField(
            model_name='contactmail',
            name='services_maintenance',
            field=models.BooleanField(default=False, verbose_name='Maintenance'),
        ),
        migrations.AlterField(
            model_name='contactmail',
            name='services_other',
            field=models.BooleanField(default=False, verbose_name='Other Services'),
        ),
        migrations.AlterField(
            model_name='contactmail',
            name='services_website',
            field=models.BooleanField(default=False, verbose_name='Website Services'),
        ),
        migrations.AlterField(
            model_name='contactmail',
            name='website',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]