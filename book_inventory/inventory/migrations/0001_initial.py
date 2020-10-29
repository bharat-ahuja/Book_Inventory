# Generated by Django 3.1.2 on 2020-10-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('google_id', models.CharField(max_length=50)),
                ('stock', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=15)),
            ],
        ),
    ]
