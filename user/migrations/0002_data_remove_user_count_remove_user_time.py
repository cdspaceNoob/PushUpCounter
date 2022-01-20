# Generated by Django 4.0.1 on 2022-01-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('time', models.CharField(max_length=255)),
                ('created', models.DateTimeField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='time',
        ),
    ]
