# Generated by Django 3.1.13 on 2021-07-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210721_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='email',
        ),
        migrations.AddField(
            model_name='mail',
            name='sender',
            field=models.EmailField(default='default_email@mail.dk', max_length=254),
        ),
        migrations.AlterField(
            model_name='mail',
            name='message',
            field=models.TextField(default='default_message'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='name',
            field=models.CharField(default='default_name', max_length=100),
        ),
        migrations.AlterField(
            model_name='mail',
            name='subject',
            field=models.CharField(default='default_subject', max_length=100),
        ),
    ]
