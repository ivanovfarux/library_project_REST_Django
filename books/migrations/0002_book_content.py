# Generated by Django 4.0 on 2023-11-14 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='test1'),
            preserve_default=False,
        ),
    ]
