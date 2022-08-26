from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserModelSerializer

class UserModelApiView(APIView):
    
    # 1. List all
    def get(self, request, *args, **kwargs):
        
        User = UserModel.objects.all()
        serializer = UserModelSerializer(User, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)