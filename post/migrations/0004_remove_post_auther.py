# Generated by Django 4.1.2 on 2022-10-06 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_auther'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='auther',
        ),
    ]