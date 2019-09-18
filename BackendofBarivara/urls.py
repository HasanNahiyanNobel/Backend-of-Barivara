from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from houses import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'houses', views.HouseViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('music/', include('music.urls')),
	# path('houses/', include('houses.urls')),
	path('houses-list/', views.HousesList.as_view()),
	path('users-list/', views.UsersList.as_view()),

	# Wire up our API using automatic URL routing.
	# Additionally, we include login URLs for the browsable API.
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
