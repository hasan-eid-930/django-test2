# Generated by Django 4.1.3 on 2022-12-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_members_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
