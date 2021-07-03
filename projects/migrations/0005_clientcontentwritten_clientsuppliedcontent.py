# Generated by Django 3.2.2 on 2021-07-03 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientContentWritten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=1200)),
                ('answer', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ClientSuppliedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project')),
                ('written_content', models.ManyToManyField(to='projects.ClientContentWritten')),
            ],
        ),
    ]