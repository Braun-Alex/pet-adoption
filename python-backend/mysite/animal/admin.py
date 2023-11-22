from django.contrib import admin

# Register your models here.

from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('breed',)


