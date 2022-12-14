# Generated by Django 4.1.1 on 2022-10-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('article', models.FileField(blank=True, upload_to='files/articles/')),
                ('image', models.ImageField(upload_to='files/images/')),
                ('link', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('auther', models.CharField(max_length=200)),
                ('time_to_read', models.CharField(max_length=200)),
            ],
        ),
    ]
