from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=("id","First_name","Last_name","Email","Organization","Contact","Date_time")