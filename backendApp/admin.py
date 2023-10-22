from django.contrib import admin
from .models import TestData, TestGivingUser, FlashCard, FlashCardTopic, FlashCardUserReaction, FlashCardSession, TestTopic


admin.site.register(TestData)
admin.site.register(TestGivingUser)
admin.site.register(FlashCard)
admin.site.register(FlashCardTopic)
admin.site.register(FlashCardUserReaction)
admin.site.register(FlashCardSession)
admin.site.register(TestTopic)
