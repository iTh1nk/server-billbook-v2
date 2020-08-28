from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api import models

from . import serializers


@api_view(["GET"])
def home(request):
    return Response({"message", "This is Activities Home!"}, status=status.HTTP_200_OK)


class GetAll(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        activities = models.Activities.objects.all()
        serializer = serializers.ActivitiesSerializer(activities, many=True)
        return Response(serializer.data)


class GetAny(APIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        activity = models.Activities.objects.get(id=pk)
        serializer = serializers.ActivitiesSerializer(activity)
        return Response(serializer.data)


class PostAll(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        print(request.data)
        serializer = serializers.ActivitiesFKSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Post Successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PutAny(APIView):
    permission_classes = (IsAdminUser,)

    def put(self, request, pk):
        activity = models.Activities.objects.get(id=pk)
        serializer = serializers.ActivitiesSerializer(activity, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Updated Successfully!', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAny(APIView):
    permission_classes = (IsAdminUser,)

    def delete(self, _, pk):
        activity = models.Activities.objects.get(id=pk)
        activity.delete()
        return Response({'success': 'Deleted Successfully!'}, status=status.HTTP_204_NO_CONTENT)
