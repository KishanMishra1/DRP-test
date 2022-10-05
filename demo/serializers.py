from rest_framework import serializers
from .models import Book,Character,Author


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields=['id','name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['id','name']

class BookSerializer(serializers.ModelSerializer):
    character=CharacterSerializer(many=True)
    authors=AuthorSerializer(many=True)
    class Meta:
        model=Book
        fields=['id','title','desc','price','published','authors','character']

