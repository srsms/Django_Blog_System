# Generated by Django 5.2.1 on 2025-05-08 09:51

import blog.custom_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_alter_tag_options_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=blog.custom_storage.MediaFileStorage(), upload_to='post_images/'),
        ),
    ]
