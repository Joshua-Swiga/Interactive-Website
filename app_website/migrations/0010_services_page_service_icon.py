# Generated by Django 5.0.1 on 2024-03-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0009_alter_events_page_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services_page',
            name='service_icon',
            field=models.ImageField(default=False, upload_to='images/service_icons'),
        ),
    ]