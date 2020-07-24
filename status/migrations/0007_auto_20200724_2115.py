# Generated by Django 3.1rc1 on 2020-07-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0006_status_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusdetail',
            name='caseid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statusdetail',
            name='error_s',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statusdetail',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
