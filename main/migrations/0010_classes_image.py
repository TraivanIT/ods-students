# Generated by Django 3.0.2 on 2020-12-10 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20201210_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='image',
            field=models.ImageField(default=1, upload_to='class/images/'),
            preserve_default=False,
        ),
    ]