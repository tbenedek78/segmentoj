# Generated by Django 3.0.7 on 2020-06-18 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0008_auto_20200618_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'permissions': (('edit', 'Can edit problem'), ('remove', 'Can delete problem'), ('view_hidden', 'Can view hidden problem'))},
        ),
    ]