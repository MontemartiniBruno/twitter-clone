# Generated by Django 4.0.4 on 2022-05-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('red_social', '0002_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]
