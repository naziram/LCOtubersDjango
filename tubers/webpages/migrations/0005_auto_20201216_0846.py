# Generated by Django 3.1.4 on 2020-12-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team_utube_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='media/team/%Y/%m/%d/'),
        ),
    ]
