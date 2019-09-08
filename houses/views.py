from django.http import HttpResponse
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from houses.models import House, User
from houses.serializer import HouseSerializer, UserSerializer


def index(request):
	html = '<h1>Hey Jude!</h1>'
	return HttpResponse(html)


class UsersList(APIView):
	def get(self, request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HousesList(APIView):
	def get(self, request):
		houses = House.objects.all()
		serializer = HouseSerializer(houses, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = HouseSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)