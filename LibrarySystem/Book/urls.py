from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('publisher', PublisherViewSet, basename='publisher')
router.register('author', AuthorViewSet, basename='author')
router.register('language', LanguageViewSet, basename='language')
router.register('Category', CategoryViewSet, basename='Category')
router.register('Section', SectionViewSet, basename='Section')
router.register('Book', BookViewSet, basename='Book')
router.register('eBook', eBookViewSet, basename='eBook')
router.register('Copies', CopiesViewSet, basename='copies')
router.register('Libraries', LibrariesViewSet, basename='Libraries')




urlpatterns = [
 path('viewset/', include(router.urls)),
 path('viewset/<int:pk>/', include(router.urls)),




]
