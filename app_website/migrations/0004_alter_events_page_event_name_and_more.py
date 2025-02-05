# Generated by Django 5.0.1 on 2024-03-03 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0003_events_page_event_date_events_page_event_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events_page',
            name='event_name',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='events_page',
            name='full_event_images',
            field=models.ImageField(default=False, upload_to='images/event_images'),
        ),
        migrations.AlterField(
            model_name='events_page',
            name='thumbnail_image',
            field=models.ImageField(default=False, upload_to='images/event_thumbnails'),
        ),
    ]
