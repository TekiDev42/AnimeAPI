# Generated by Django 4.0.6 on 2022-07-30 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_anime_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plateforme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plateforme', models.CharField(max_length=64, null=True)),
                ('plateforme_url', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='anime',
            name='plateforme_url',
        ),
        migrations.AlterField(
            model_name='anime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='anime',
            name='plateforme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.plateforme'),
        ),
    ]