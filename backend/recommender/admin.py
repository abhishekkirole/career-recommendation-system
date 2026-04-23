from django.contrib import admin
from .models import CareerPath, UserProfile

@admin.register(CareerPath)
class CareerPathAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'demand_level', 'salary_range']
    list_filter = ['category', 'demand_level']
    search_fields = ['title', 'description']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'experience_level', 'created_at']
    list_filter = ['experience_level']
    search_fields = ['name', 'email', 'skills']