# Generated by Django 3.0.7 on 2020-07-16 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0011_auto_20200619_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='show_id',
            new_name='pid',
        ),
    ]
