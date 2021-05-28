# Generated by Django 3.2.2 on 2021-05-28 15:02

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='', max_length=250)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('background', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('tags', models.ManyToManyField(related_name='blog_tags', to='tags.BlogTag')),
            ],
        ),
    ]
