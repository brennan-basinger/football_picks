# picks/admin.py
from django.contrib import admin
from .models import User, Game, Pick

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('team', 'week', 'opponent')

@admin.register(Pick)
class PickAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'pick')
    list_filter = ('pick', 'game__week', 'user')
