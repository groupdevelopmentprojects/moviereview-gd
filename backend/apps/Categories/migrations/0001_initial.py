# Generated by Django 3.2.4 on 2022-08-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Datetime')),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]