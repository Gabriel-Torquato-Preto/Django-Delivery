# Generated by Django 4.2.4 on 2023-08-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='insert a e-mail', max_length=254),
        ),
    ]
