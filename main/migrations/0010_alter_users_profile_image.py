# Generated by Django 5.1.1 on 2024-10-04 16:08

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_users_city_or_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=90, scale=None, size=[100, 100], upload_to='profiles/'),
        ),
    ]
