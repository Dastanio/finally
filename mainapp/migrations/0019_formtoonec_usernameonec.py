# Generated by Django 3.0.8 on 2020-08-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_formtoonec_userid2'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtoonec',
            name='usernameonec',
            field=models.CharField(default='', max_length=500, verbose_name='UserName'),
        ),
    ]
