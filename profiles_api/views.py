from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    ''' TEst API View '''
    serializer_class = serializers.HelloSerializer


    def get(self,request,format=None):
        ''' Returns a APIViews features'''
        an_apiview = [
            'Users HTTP Methods as function (get,post,patch,put,Delete',
            'Similar to Django Views',
            'Gives you the most control over the application logic',
            'Is Mapped manually to URLS',
        ]
        return Response({'message':'Hello !','an_apiview' : an_apiview})


    def post(self,request):
        ''' Create a Hello name messsage with our Serializer'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        ''' Handle Updating the Objects'''
        return Response ({'method':'PUT'})

    def patch(self,request,pk=None):
        '''Handle Partial update of an Object'''
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        ''' Delete an Object'''
        return Response({'method':'DELETE'})

