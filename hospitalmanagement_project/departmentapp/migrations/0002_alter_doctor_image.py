# Generated by Django 3.2.4 on 2021-06-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='doctor'),
        ),
    ]
