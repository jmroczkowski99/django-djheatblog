# Generated by Django 4.2.7 on 2023-11-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.TextField(blank=True),
        ),
    ]