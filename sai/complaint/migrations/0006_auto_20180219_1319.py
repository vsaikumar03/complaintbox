# Generated by Django 2.0.1 on 2018-02-19 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0005_choice_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='choiceVote',
        ),
        migrations.RemoveField(
            model_name='votes',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Votes',
        ),
    ]
