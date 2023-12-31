# Generated by Django 4.2.3 on 2023-11-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=78)),
                ('Place', models.CharField(max_length=78)),
                ('Phone', models.IntegerField()),
                ('Game', models.CharField(max_length=98)),
                ('Date_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Place', models.TextField()),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Username', models.CharField(max_length=78)),
                ('Password', models.CharField(max_length=89)),
            ],
        ),
    ]
