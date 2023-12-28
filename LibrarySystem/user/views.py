from .models import *
from .Serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')

            user = User.objects.get(username=username)
            if not user.check_password(old_password):
                return Response({'detail': 'Invalid old password'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenderViewSet(viewsets.ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class FacultyViewSet(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()


class SemesterViewSet(viewsets.ModelViewSet):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAccountViewSet(viewsets.ModelViewSet):
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()


class DespositesViewSet(viewsets.ModelViewSet):
    serializer_class = DespositesSerializer
    queryset = Desposites.objects.all()


class NewViewSet(viewsets.ModelViewSet):
    serializer_class = NewSerializer
    queryset = New.objects.all()
