# Generated by Django 3.2.8 on 2022-07-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'user profile', 'verbose_name_plural': 'user profiles'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x0000016204B4B850> <django.db.models.query_utils.DeferredAttribute object at 0x0000016204B4B580>', max_length=100, verbose_name='Display name'),
        ),
    ]
