# Generated by Django 5.0.4 on 2024-04-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_author_portrait'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='category name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
    ]
