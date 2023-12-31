# Generated by Django 4.1.3 on 2023-09-13 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0019_alter_session_endtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashCardUserReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default=1, max_length=4)),
                ('reaction', models.CharField(default='undeclaired', max_length=7)),
                ('dateTime', models.DateTimeField(default=datetime.date(2023, 9, 13))),
                ('relatedCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.flashcard')),
            ],
        ),
        migrations.RenameModel(
            old_name='Session',
            new_name='FlashCardSession',
        ),
        migrations.DeleteModel(
            name='UserReaction',
        ),
        migrations.AddField(
            model_name='flashcarduserreaction',
            name='session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backendApp.flashcardsession'),
        ),
    ]
