from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from api import models
from api.pagination import CustomPagination

from . import serializers


@api_view(["GET"])
def home(request):
    return Response({"message": "This is Statements Home!"}, status=status.HTTP_200_OK)


class GetAll(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        statements = models.Statements.objects.all().order_by('-createdAt')
        serializer = serializers.StatementsSerializer(statements, many=True)
        return Response(serializer.data)


class GetPage(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get(self, request):
        statements = models.Statements.objects.all().order_by('-createdAt')
        page = self.paginate_queryset(statements)

        if page is not None:
            serializer = serializers.StatementsSerializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data
        else:
            serializer = serializers.StatementsSerializer(
                statements, many=True)
            data = serializer.data

        return Response(data)


class GetAny(APIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        statement = models.Statements.objects.get(id=pk)
        serializer = serializers.StatementsSerializer(statement)
        return Response(serializer.data)


class PostAll(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        print(request.data)
        serializer = serializers.StatementsFKSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Post Successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PutAny(APIView):
    permission_classes = (IsAdminUser,)

    def put(self, request, pk):
        statement = models.Statements.objects.get(id=pk)
        serializer = serializers.StatementsSerializer(statement, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Updated Successfully!', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAny(APIView):
    permission_classes = (IsAdminUser,)

    def delete(self, _, pk):
        statement = models.Statements.objects.get(id=pk)
        statement.delete()
        return Response({'success': 'Deleted Successfully!'}, status=status.HTTP_204_NO_CONTENT)
