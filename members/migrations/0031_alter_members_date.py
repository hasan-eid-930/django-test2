# Generated by Django 4.1.3 on 2023-01-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0030_alter_members_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='date',
            field=models.DateField(),
        ),
    ]
