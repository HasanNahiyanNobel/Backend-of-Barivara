from django.contrib import admin

# Register your models here.
from houses.models import House, User

admin.site.register(House)
admin.site.register(User)