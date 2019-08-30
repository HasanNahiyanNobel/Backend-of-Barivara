from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class MusicList(APIView):
	def get(self):
		return Response("hau")
