# Generated by Django 4.0.6 on 2022-07-29 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_anime_plateforme_url_alter_anime_plateforme_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='user',
        ),
    ]