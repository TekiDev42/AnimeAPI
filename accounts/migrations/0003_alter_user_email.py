# Generated by Django 4.0.6 on 2022-07-29 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()], verbose_name='email address'),
        ),
    ]
