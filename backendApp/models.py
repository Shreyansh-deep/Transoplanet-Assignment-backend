from django.db import models
from datetime import date
class TestTopic(models.Model):
    topicName =  models.CharField(max_length=100, default = 'natural resources')
    topicDescription =  models.CharField(max_length=100, default = 'this is default description')
class TestData(models.Model):
    topic = models.ForeignKey(TestTopic, on_delete=models.CASCADE, default=1)
    testName = models.CharField(max_length=100, default = 'testDefaultName')
    testType = models.CharField(max_length=100, default = 'objective')
    questionNumbers = models.IntegerField(max_length=3, default=50)
    duration = models.IntegerField(max_length=3, default=1)
    attempted = models.BooleanField(default=True)
    testStatus = models.IntegerField(max_length=1, default=1)
    def __str__(self):
        return f"{self.topic.topicName}-{self.testType}"

class TestGivingUser(models.Model):
    testAssigned = models.ForeignKey( TestData , on_delete=models.CASCADE)

class FlashCardTopic(models.Model):
    topic = models.CharField(max_length = 20, blank=False)
    desc= models.CharField(max_length = 500, blank=False)

class FlashCardSession(models.Model):
    topic = models.ForeignKey(FlashCardTopic, on_delete=models.CASCADE, default=None);
    userId = models.IntegerField(max_length=4, default=1);
    startTime = models.DateTimeField(auto_now_add=False)
    endTime = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    reactionRecorded = models.CharField(max_length = 500, null=True, blank=True)

class FlashCard(models.Model):
    cardTopic = models.ForeignKey(FlashCardTopic, on_delete=models.CASCADE);
    slNumber = models.IntegerField(max_length=3, default='0');
    cardData = models.CharField(max_length=700 );

class FlashCardUserReaction(models.Model):
    userId = models.IntegerField(max_length=4, default=1);
    reaction = models.CharField(max_length=7, default = 'undeclaired')
    relatedCard = models.ForeignKey(FlashCard, on_delete=models.CASCADE)
    dateTime = models.DateTimeField( default = date.today() )
    session = models.ForeignKey(FlashCardSession, on_delete=models.CASCADE , default=None)
