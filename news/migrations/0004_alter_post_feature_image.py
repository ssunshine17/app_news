# Generated by Django 4.0.3 on 2022-04-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(upload_to='news/static/img_post'),
        ),
    ]