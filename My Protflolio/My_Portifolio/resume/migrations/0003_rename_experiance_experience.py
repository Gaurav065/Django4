# Generated by Django 3.2.5 on 2022-08-26 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('resume', '0002_alter_skill_typeof'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='experiance',
            new_name='experience',
        ),
    ]