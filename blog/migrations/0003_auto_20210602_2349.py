# Generated by Django 3.2.2 on 2021-06-02 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210602_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='background',
            field=models.CharField(blank=True, default='', help_text='http://...', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blog_tags', to='blog.BlogTag'),
        ),
    ]
