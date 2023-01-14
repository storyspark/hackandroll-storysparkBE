from rest_framework import serializers
from .models import Storyboard

class StoryboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storyboard
        fields = ['id', 'author', 'title', 'category', 'tone', 'type', 'storyPrompt', 'imagePrompt', 'isPrivate', 'storyResult', 'imageUrl']
