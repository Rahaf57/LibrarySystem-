from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('Gender', GenderViewSet, basename='Gender')
router.register('Role', RoleViewSet, basename='Role')
router.register('City', CityViewSet, basename='City')
router.register('Faculty', FacultyViewSet, basename='Faculty')
router.register('Semester', SemesterViewSet, basename='Semester')
router.register('User', UserViewSet, basename='User')
router.register('UserAccount', UserAccountViewSet, basename='UserAccount')
router.register('Desposites', DespositesViewSet, basename='Desposites')
router.register('New', NewViewSet, basename='New')




urlpatterns = [
 path('viewset2/', include(router.urls)),
 path('viewset2/<int:pk>/', include(router.urls)),
 path('register/', register_user, name='register'),
 path('login/', user_login, name='login'),
 path('logout/', user_logout, name='logout'),
path('change-password/', ChangePasswordView.as_view(), name='change-password'),




]
