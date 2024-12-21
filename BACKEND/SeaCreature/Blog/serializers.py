from rest_framework import serializers
from .models import *

#serializer for seaCreatures
class SeaCreatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeaCreature
        fields = '__all__'


#Serializer for Blogpost
class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'

#Serializer for Comment
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'