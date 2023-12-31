# Generated by Django 4.2.4 on 2023-08-10 17:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(default='insert a name', max_length=100)),
                ('password', models.TextField(default='insert a password', max_length=100)),
                ('phone_number', models.TextField(default='insert a phone number', max_length=100)),
            ],
        ),
    ]
