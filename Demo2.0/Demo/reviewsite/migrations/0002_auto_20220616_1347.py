# Generated by Django 3.2.5 on 2022-06-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperinfo',
            name='state',
            field=models.CharField(default='未分配', max_length=20),
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='position',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='region',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='sex',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='user_type',
            field=models.CharField(max_length=20),
        ),
    ]