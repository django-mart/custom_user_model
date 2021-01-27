from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from django.contrib.auth import get_user_model

# Create your views here.
class Register(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "message": "try to access this as post api"
            },
            status=status.HTTP_200_OK
        )
    
    def post(self, request, format=None):
        try:
            userData = JSONParser().parse(request)
            
            user = get_user_model().objects.create_user(
                email=userData["email"],
                password=userData["password"]
            )
            user.save()

            return Response(
                {
                    "message": "new user created successfully"
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": "error occured",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )