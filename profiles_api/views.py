from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """Test Api View"""
  def get(self, request, format= None):
    """Return a list of ApiView Features"""
    an_apiview = [
      'Uses HTTP methods as functions (get, post, patch, put, delete)',
      'Is similar to a tradicional Django View',
      'Give you the most control over your application logic',
      'Is mapped manually to URLs',
    ]
    return Response({'mensage': 'Hello!', 'an_apiview': an_apiview}) #Precisa estar em uma lista ou dicionario para converter para json
