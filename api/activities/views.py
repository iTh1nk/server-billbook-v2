from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(["GET"])
def home(request):
    return Response({"message", "This is Activities Home!"}, status=status.HTTP_200_OK)
