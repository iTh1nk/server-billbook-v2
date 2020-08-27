from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.user.serializers import UserLoginSerializer

from .serializers import UserRegistrationSerializer

from api.models import UserProfile


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered successfully!'
        }

        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in successfully!',
            'token': serializer.data['token']
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


# User Profile View
class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'True',
                'status code': status_code,
                'message': 'User profile fetched successfully!',
                'data': [
                    {
                        'first_name': user_profile.first_name,
                        'last_name': user_profile.last_name,
                        'phone_number': user_profile.phone_number,
                        'age': user_profile.age,
                        'gender': user_profile.gender
                    }
                ]
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'False',
                'status code': status_code,
                'message': 'User does not exists!',
                'error': str(e)
            }
        return Response(response, status=status_code)
