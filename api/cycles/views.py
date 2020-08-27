from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api import models
from . import serializers


@api_view(["GET"])
def home(request):
    return Response({"message", "This is Cycles Home!"}, status=status.HTTP_200_OK)


class CyclesGetPost(APIView):
    def get(self, request):
        cycles = models.Cycles.objects.all()
        serializer = serializers.CyclesSerializer(cycles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CyclesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CyclesGetPutDelete(APIView):
    def get(self, request, pk):
        cycle = models.Cycles.objects.get(id=pk)
        serializer = serializers.CyclesSerializer(cycle)
        return Response(serializer.data)

    def put(self, request, pk):
        cycle = models.Cycles.objects.get(id=pk)
        serializer = serializers.CyclesSerializer(cycle, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        cycle = models.Cycles.objects.get(id=pk)
        cycle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
