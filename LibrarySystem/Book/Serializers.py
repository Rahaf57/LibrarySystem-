from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'publisher', 'location']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category', 'category_persion']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'section', 'section_persion', 'category']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'signatory', 'title', 'isbn', 'peges', 'publication_year', 'language', 'description', 'edition',
                  'author', 'publisher', 'faculty', 'section', 'category']


class eBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = eBook
        fields = ['id', 'book', 'extension']


class CopiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copies
        fields = ['book', 'status']


class LibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libraries
        fields = ['id', 'faculty', 'content', 'content_persian', 'privacy', 'privacy_persian', 'service',
                  'service_persian', 'email']
