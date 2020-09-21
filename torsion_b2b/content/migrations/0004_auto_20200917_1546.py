# Generated by Django 2.2.13 on 2020-09-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_ratingcontent_ratingstar_reviewcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='comment_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='comment_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='comment_uk',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='full_text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='full_text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='full_text_uk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='intro_text_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='intro_text_ru',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='intro_text_uk',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_description_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_description_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_description_uk',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_keyword_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_keyword_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_keyword_uk',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_title_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_title_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='meta_tag_title_uk',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='title_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='title_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='title_uk',
            field=models.CharField(max_length=500, null=True),
        ),
    ]