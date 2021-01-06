from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from api import models
from api.permissions import IsOwnerOrReadOnly

from . import serializers


@api_view(["GET"])
def home(request):
    return Response({"message": "This is APNsToken Home!"}, status=status.HTTP_200_OK)


class GetAll(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        apnsTokens = models.APNsToken.objects.all()
        serializer = serializers.ApnsTokenSerializer(apnsTokens, many=True)
        return Response(serializer.data)


class GetAny(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, pk):
        apnsTokens = models.APNsToken.objects.get(id=pk)
        serializer = serializers.ApnsTokenSerializer(apnsTokens)
        return Response(serializer.data)


class PostAll(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = serializers.ApnsTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Post Successfully!', 'data': serializer.data, 'status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        return Response({'Error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAny(APIView):
    permission_classes = (IsAdminUser,)

    def delete(self, _, pk):
        apnsTokens = models.APNsToken.objects.get(id=pk)
        apnsTokens.delete()
        return Response({'success': 'Deleted Successfully!', 'status': status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)