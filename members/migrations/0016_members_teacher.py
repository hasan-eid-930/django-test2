# Generated by Django 4.1.3 on 2022-12-27 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='teacher',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='members.teacher'),
        ),
    ]
