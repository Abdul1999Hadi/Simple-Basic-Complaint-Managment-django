# Generated by Django 4.2.6 on 2023-12-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0005_alter_usercomplaint_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomplaint',
            name='complaint_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]