# Generated by Django 3.1.6 on 2021-04-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name="person's first name")),
                ('photo', models.ImageField(upload_to='kkimages')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
