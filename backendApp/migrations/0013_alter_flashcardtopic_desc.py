# Generated by Django 4.1.3 on 2023-09-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0012_alter_userreaction_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcardtopic',
            name='desc',
            field=models.CharField(blank=True, default='Description for default', max_length=500),
        ),
    ]