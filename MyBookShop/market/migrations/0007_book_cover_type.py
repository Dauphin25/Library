# Generated by Django 5.0.4 on 2024-04-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_remove_book_category_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_type',
            field=models.CharField(choices=[('hard', 'Hardcover'), ('soft', 'Softcover'), ('paperback', 'Paperback'), ('spiral', 'Spiral-bound'), ('board', 'Board book'), ('cloth', 'Clothbound'), ('leather', 'Leather-bound'), ('other', 'Other')], default='other', max_length=10),
        ),
    ]
