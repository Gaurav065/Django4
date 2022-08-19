# Generated by Django 3.2.5 on 2022-08-17 13:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0003_party_member_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=125)),
                ('party_level', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100)])),
                ('party_size', models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(10)])),
                ('party_rank', models.CharField(default='G', max_length=1)),
            ],
        ),
    ]