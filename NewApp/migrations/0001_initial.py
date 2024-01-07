# Generated by Django 4.2.5 on 2023-09-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='categories')),
            ],
        ),
    ]
