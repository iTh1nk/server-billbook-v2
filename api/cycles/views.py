from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api import models
from api.permissions import IsOwnerOrReadOnly

from . import serializers


@api_view(["GET"])
def home(request):
    return Response({"message": "This is Cycles Home!"}, status=status.HTTP_200_OK)


class GetAll(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def get(self, request):
        cycles = models.Cycles.objects.all().order_by('date')
        serializer = serializers.CyclesFKSerializer(cycles, many=True)
        return Response(serializer.data)


class GetAny(APIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        cycle = models.Cycles.objects.get(id=pk)
        serializer = serializers.CyclesFKSerializer(cycle)
        # self.check_object_permissions(self.request, {'user': cycle.date})
        return Response(serializer.data)


class PostAll(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = serializers.CyclesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Post Successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PutAny(APIView):
    permission_classes = (IsAdminUser,)

    def put(self, request, pk):
        cycle = models.Cycles.objects.get(id=pk)
        serializer = serializers.CyclesSerializer(cycle, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Updated Successfully!', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAny(APIView):
    permission_classes = (IsAdminUser,)

    def delete(self, _, pk):
        cycle = models.Cycles.objects.get(id=pk)
        cycle.delete()
        return Response({'success': 'Deleted Successfully!'}, status=status.HTTP_204_NO_CONTENT)
