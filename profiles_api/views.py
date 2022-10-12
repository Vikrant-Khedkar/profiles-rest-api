import imp
from tkinter.messagebox import RETRY
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
import urllib.request


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer


    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview= [ 'uses HTTP methods as functions(get,post,patch,put,delete',
        'is similar to a tradional django view',
        'gives you most control over your application',
        'is manually mapped to URLs',]
        return Response({'message':'Hello!','an_apiview':an_apiview})
    
    def post(self,request):
        """Create a hello message with our name"""
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
