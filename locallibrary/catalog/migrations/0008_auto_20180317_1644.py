# Generated by Django 2.0.2 on 2018-03-17 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20180317_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='book',
            name='like',
        ),
    ]
