from django.contrib import admin
from django.urls import path, include

from houses import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('music/', include('music.urls')),
	path('houses/', include('houses.urls')),
	path('houses-list/', views.HousesList.as_view()),
	path('users-list/', views.UsersList.as_view()),
]
