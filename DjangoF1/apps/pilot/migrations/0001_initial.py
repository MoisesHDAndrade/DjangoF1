# Generated by Django 3.1.7 on 2021-03-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('forename', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='pilot/<django.db.models.fields.CharField>/')),
            ],
        ),
    ]
