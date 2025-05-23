from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
  """Test Api View"""
  serializer_class = serializers.HelloSerializer
  def get(self, request, format= None):
    """Return a list of ApiView Features"""
    an_apiview = [
      'Uses HTTP methods as functions (get, post, patch, put, delete)',
      'Is similar to a tradicional Django View',
      'Give you the most control over your application logic',
      'Is mapped manually to URLs',
    ]
    return Response({'mensage': 'Hello!', 'an_apiview': an_apiview}) #Precisa estar em uma lista ou dicionario para converter para json
  def post(self,request):
    """Create a hello mensage with our name"""
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return Response({'message': message})
    else:
      return Response(serializer.errors,
             status=status.HTTP_400_BAD_REQUEST)