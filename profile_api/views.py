from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializer


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return list of APIView features"""
        an_apiview = [
                        "Azad aleyes Salam",
                        'Vitamin c',
                        'POker master',
                        'develper',
                        "DevOPs",
                      ]

        return Response({"message": "Hello", 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message': message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
         )

    def put(self, request, pk=None):
        """Handle updating"""
        return Response ({"method": 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating"""
        return Response ({"method": 'PATCH'})


        def delete(self, request, pk=None):
            """Delete an Object"""
            return Response ({"method": 'DELETE'})
