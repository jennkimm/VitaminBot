# Generated by Django 2.2.7 on 2020-03-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawled_data', '0005_auto_20200305_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='boarddata',
            name='image',
            field=models.URLField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='boarddata',
            name='price',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
