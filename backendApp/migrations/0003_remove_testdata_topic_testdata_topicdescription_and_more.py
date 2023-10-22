# Generated by Django 4.1.3 on 2023-04-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0002_testdata_testname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testdata',
            name='topic',
        ),
        migrations.AddField(
            model_name='testdata',
            name='topicDescription',
            field=models.CharField(default='this is default description', max_length=100),
        ),
        migrations.AddField(
            model_name='testdata',
            name='topicName',
            field=models.CharField(default='natural resources', max_length=100),
        ),
        migrations.DeleteModel(
            name='TestTopic',
        ),
    ]