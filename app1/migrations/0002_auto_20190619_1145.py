# Generated by Django 2.2.2 on 2019-06-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='ads')),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]