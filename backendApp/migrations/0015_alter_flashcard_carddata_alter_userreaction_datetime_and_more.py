# Generated by Django 4.1.3 on 2023-09-11 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0014_userreaction_datetime_alter_flashcardtopic_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='cardData',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='userreaction',
            name='dateTime',
            field=models.DateTimeField(default=datetime.date(2023, 9, 11)),
        ),
        migrations.AlterField(
            model_name='userreaction',
            name='reaction',
            field=models.CharField(default='Undeclaired', max_length=7),
        ),
    ]
