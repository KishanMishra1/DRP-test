# Generated by Django 3.2.16 on 2022-10-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20221005_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn_10', models.CharField(blank=True, max_length=10)),
                ('isbn_13', models.CharField(blank=True, max_length=13)),
            ],
        ),
    ]