# Generated by Django 2.2.6 on 2020-09-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200924_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_auth', models.BooleanField(default=False)),
            ],
        ),
    ]
