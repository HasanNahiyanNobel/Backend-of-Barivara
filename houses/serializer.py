from rest_framework import serializers

from .models import House


class HomeSerializer(serializers.ModelSerializer):
	class Meta:
		model = House
		fields = '__all__'
