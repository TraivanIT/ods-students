# Generated by Django 3.0.2 on 2020-12-10 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='book/images/'),
        ),
    ]
