# Generated by Django 3.2.2 on 2021-05-28 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('rating', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')], default=0)),
                ('url', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('backgroundImage', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('backgroundImageUpload', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('repo', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('core_deps', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
        ),
    ]
