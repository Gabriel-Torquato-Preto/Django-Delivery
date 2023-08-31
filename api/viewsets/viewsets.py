from rest_framework import viewsets
from ..models import User, Menu
from ..serializers import serializer
from rest_framework.response import Response
from rest_framework import status

class userViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.userSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     if User.objects.filter(email = serializer.data["email"]):
    #         return Response("Usuário já cadastrado!" , status=status.HTTP_409_CONFLICT)
    #     else:
    #         serializer.save()
    #         return Response("Usuário cadastrado com sucesso!",status=status.HTTP_201_CREATED)

class MenuViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = serializer.MenuSerialzer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception = True)
    #     if Menu.objects.filter(name = request.data["name"]):
    #         return Response("Lanche já cadastrado em nosso cardápio!",status=status.HTTP_409_CONFLICT)
    #     elif (float(request.data["price"])<= 0):
    #         return   Response("Por favor coloque um preço adequado não damos coisas de graça!", status= status.HTTP_400_BAD_REQUEST)
    #     else:
    #         serializer.save()
    #         return Response("Lanche registrado no cardápio com sucesso!",status=status.HTTP_201_CREATED)
