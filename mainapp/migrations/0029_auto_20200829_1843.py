# Generated by Django 3.1 on 2020-08-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_auto_20200829_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='allper',
            name='password',
            field=models.CharField(default='', max_length=500, verbose_name='password'),
        ),
        migrations.AddField(
            model_name='allper',
            name='username',
            field=models.CharField(default='', max_length=500, verbose_name='username'),
        ),
        migrations.AddField(
            model_name='month',
            name='password',
            field=models.CharField(default='', max_length=500, verbose_name='password'),
        ),
        migrations.AddField(
            model_name='month',
            name='username',
            field=models.CharField(default='', max_length=500, verbose_name='username'),
        ),
        migrations.AddField(
            model_name='week',
            name='password',
            field=models.CharField(default='', max_length=500, verbose_name='password'),
        ),
        migrations.AddField(
            model_name='week',
            name='username',
            field=models.CharField(default='', max_length=500, verbose_name='username'),
        ),
    ]