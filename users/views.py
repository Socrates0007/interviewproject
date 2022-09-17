from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserModelSerializer

# Create your views here.
#get all directories
@api_view(["GET"])
def home_view(request):
    routes={
        "/register/":"register new users",
        "/login/":"log a user in to get access and refresh token",
        "/token/refresh":"get a new access token with a refresh token",
        "/template/":"get all templates with access token and add new templates",
        "/template/id":"fettch a single template, update and delete"

    }
    return Response(routes)






@api_view(['GET','POST'])
def users_view(request):
    if request.method=="GET":
        users=User.objects.all()
        serializer_class=UserModelSerializer(users,many=True)
        return Response(serializer_class.data)
    if request.method=='POST':
        serializer_class=UserModelSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)

#wow i love my jobs
#wow i love my job twice