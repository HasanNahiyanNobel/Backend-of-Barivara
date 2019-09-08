from django.contrib import admin

# Register your models here.
from houses.models import House, User


class HouseAdmin(admin.ModelAdmin):
	list_display = [field.name for field in House._meta.get_fields()]


class UserAdmin(admin.ModelAdmin):
	list_display = [field.name for field in User._meta.get_fields()]


admin.site.register(House, HouseAdmin)
admin.site.register(User, UserAdmin)
