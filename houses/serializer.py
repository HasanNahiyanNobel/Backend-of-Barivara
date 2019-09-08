from rest_framework import serializers

from .models import House, User


class HouseSerializer(serializers.ModelSerializer):
	class Meta:
		model = House
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
