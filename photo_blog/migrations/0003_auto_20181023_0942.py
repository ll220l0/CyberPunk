# Generated by Django 2.1.2 on 2018-10-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_blog', '0002_auto_20181018_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
