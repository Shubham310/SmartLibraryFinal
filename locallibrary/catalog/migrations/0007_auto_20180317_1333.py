# Generated by Django 2.0.2 on 2018-03-17 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20180317_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='dilike',
            new_name='dislike',
        ),
    ]
