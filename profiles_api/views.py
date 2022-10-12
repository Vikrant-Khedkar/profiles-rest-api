from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self,resuquest,format=None):
        """Returns a list of APIView features"""
        an_apiview= [ 'uses HTTP methods as functions(get,post,patch,put,delete',
        'is similar to a tradional django view',
        'gives you most control over your application',
        'is manually mapped to URLs',]
        return Response({'message':'Hello!','an_apiview':an_apiview})
