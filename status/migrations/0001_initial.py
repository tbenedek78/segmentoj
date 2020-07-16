# Generated by Django 3.0.7 on 2020-07-16 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0012_auto_20200716_1903'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('memory', models.IntegerField(default=0)),
                ('input_s', models.CharField(max_length=100)),
                ('output_s', models.CharField(max_length=100)),
                ('answer_s', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('memory', models.IntegerField(default=0)),
                ('lang', models.IntegerField(default=0)),
                ('code', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('judge_detail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='status.StatusDetail')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
            ],
        ),
    ]
