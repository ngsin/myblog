# Generated by Django 2.2.1 on 2019-10-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0002_auto_20191011_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='examplemodel',
            name='update_time',
            field=models.DateTimeField(),
        ),
    ]
