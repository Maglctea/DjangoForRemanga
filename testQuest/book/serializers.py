from rest_framework import serializers
from .models import Title, Chapter, Volume, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['number', 'like_counter', 'views_counter']


class ChapterRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):
    chapters = ChapterListSerializer(many=True)

    class Meta:
        model = Volume
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    volumes = VolumeSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Title
        fields = '__all__'