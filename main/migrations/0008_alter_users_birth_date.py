# Generated by Django 5.1.1 on 2024-10-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_users_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birth_date',
            field=models.CharField(max_length=100),
        ),
    ]
