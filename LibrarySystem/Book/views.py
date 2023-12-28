from .models import *
from .Serializers import *
from rest_framework import viewsets


class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class eBookViewSet(viewsets.ModelViewSet):
    serializer_class = eBookSerializer
    queryset = eBook.objects.all()


class CopiesViewSet(viewsets.ModelViewSet):
    serializer_class = CopiesSerializer
    queryset = Copies.objects.all()


class LibrariesViewSet(viewsets.ModelViewSet):
    serializer_class = LibrariesSerializer
    queryset = Libraries.objects.all()
