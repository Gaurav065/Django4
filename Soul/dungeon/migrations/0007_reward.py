# Generated by Django 3.2.5 on 2022-08-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0006_rename_quests_quest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_reward', models.CharField(default='10 coppers', max_length=50)),
            ],
        ),
    ]
