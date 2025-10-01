from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team', 'created_at')
    search_fields = ('name', 'email')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'duration', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('user', 'activity')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'total_minutes', 'rank')
    list_filter = ('team',)
    ordering = ('rank',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'difficulty', 'suggested_for')
    list_filter = ('difficulty',)
    search_fields = ('name', 'suggested_for')
