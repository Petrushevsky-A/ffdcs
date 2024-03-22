from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from models import *
from serializer import *

class Rights(APIView):

    def get(self, request, *args, **kwargs):
        Access.objects.filter()
        # services for all user

        # user

        # role

        # organization structure
        return Response()
    def post(self, request, *args, **kwargs):
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=es.errors, status=status.HTTP_400_BAD_REQUEST)
