# Generated by Django 4.1.3 on 2022-12-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_alter_members_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='age',
            field=models.IntegerField(default=30),
        ),
    ]
