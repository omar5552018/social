# Generated by Django 2.0.7 on 2018-10-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20181010_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(blank=True, upload_to='Posts'),
        ),
    ]
