# Generated by Django 2.0.7 on 2018-07-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_image',
            field=models.ImageField(default=1, upload_to='featued_image'),
            preserve_default=False,
        ),
    ]