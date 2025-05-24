from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
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
    
  def put(self,request,pk=None):
    """Handle updating an object"""
    return Response({'method': 'PUT'})
  
  def patch(self,request,pk=None):
    """Handle a partial update of an object"""
    return Response({'method': 'PATCH'})
  
  def delete(self,request,pk=None):
    """Delete an object"""
    return Response({'method': 'DELETE'})
  

class HelloViewSet(viewsets.ViewSet):
  """TEST API VIEWSET"""
  serializer_class = serializers.HelloSerializer
  def list(self,request):
    """Return a hello message"""
    a_viewset = [
      'Uses actions (list, create, retrieve, update, partial_update)',
      'Automatically maps to URLs using Routers',
      'Provides more functionality with less code',
    ]
    return Response({'message': 'Hello!', 'a_viewset': a_viewset})
  
  def create(self,request):
    """Create a new hello message"""
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}!'
      return Response({'message': message})
    else:
      return Response(serializer.errors,
             status=status.HTTP_400_BAD_REQUEST)
    
  def retrieve(self,request,pk=None): # Busca o objeto
    """Handle getting an object by its ID""" 
    return Response({'http_method': 'GET'})
  
  def update(self,request,pk=None): # Atualiza o objeto
    """Handle updating an object"""
    return Response({'http_method': 'PUT'})
  
  def partial_update(self,request,pk=None): # Atualiza apenas parte do objeto
    """Handle updating part of an object"""
    return Response({'http_method': 'PATCH'})
  
  def destroy(self,request,pk=None): # Deleta o objeto
    """Handle removing an object"""
    return Response({'http_method': 'DELETE'})
    
