# Generated by Django 4.1.3 on 2023-09-03 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0008_alter_flashcard_carddata_alter_flashcard_cardtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashCardTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicName', models.CharField(default='Chemicals', max_length=100)),
                ('description', models.CharField(default='description of chemicals', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(default=None, max_length=20)),
                ('flascard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.flashcard')),
            ],
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='cardTopic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendApp.flashcardtopic'),
        ),
    ]
