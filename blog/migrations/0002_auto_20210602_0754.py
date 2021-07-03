# Generated by Django 3.2.2 on 2021-06-02 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_alter_blogtag_usage_count'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('tag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tags.tag')),
                ('usage_count', models.PositiveIntegerField(default=0)),
            ],
            bases=('tags.tag',),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(related_name='blog_tags', to='blog.BlogTag'),
        ),
    ]