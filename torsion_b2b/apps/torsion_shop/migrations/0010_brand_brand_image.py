# Generated by Django 3.0.6 on 2020-05-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torsion_shop', '0009_auto_20200509_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_image',
            field=models.ImageField(blank=True, null=True, upload_to='content/brand_image/'),
        ),
    ]