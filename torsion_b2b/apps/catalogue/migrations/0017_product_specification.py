# Generated by Django 2.2.13 on 2020-06-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_auto_20190327_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
