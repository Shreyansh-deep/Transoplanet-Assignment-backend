# Generated by Django 4.1.3 on 2023-08-31 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0007_flashcard_cardtopic_flashcard_slnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='cardData',
            field=models.CharField(default="{'frontBg' :'#F5F7E4', 'frontContent': '1st front side', 'backBg':'blue', 'backContent':'1st back side'}", max_length=700),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='cardTopic',
            field=models.CharField(default='natural resources', max_length=700),
        ),
    ]
