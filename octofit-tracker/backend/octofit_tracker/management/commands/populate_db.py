from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

from django.contrib.auth import get_user_model
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        with connection.cursor() as cursor:
            cursor.execute('DROP COLLECTION IF EXISTS users')
            cursor.execute('DROP COLLECTION IF EXISTS teams')
            cursor.execute('DROP COLLECTION IF EXISTS activities')
            cursor.execute('DROP COLLECTION IF EXISTS leaderboard')
            cursor.execute('DROP COLLECTION IF EXISTS workouts')

        # Insert test data
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
        ]
        teams = [
            {"name": "Marvel", "members": ["Iron Man", "Captain America", "Black Widow"]},
            {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
        ]
        activities = [
            {"user": "Superman", "activity": "Flying", "duration": 120},
            {"user": "Iron Man", "activity": "Running", "duration": 60},
        ]
        leaderboard = [
            {"team": "Marvel", "points": 300},
            {"team": "DC", "points": 250},
        ]
        workouts = [
            {"name": "Strength Training", "suggested_for": "Superman"},
            {"name": "Cardio", "suggested_for": "Iron Man"},
        ]

        with connection.cursor() as cursor:
            cursor.execute('CREATE COLLECTION users')
            cursor.execute('CREATE COLLECTION teams')
            cursor.execute('CREATE COLLECTION activities')
            cursor.execute('CREATE COLLECTION leaderboard')
            cursor.execute('CREATE COLLECTION workouts')
            for user in users:
                cursor.execute('INSERT INTO users (name, email, team) VALUES (%s, %s, %s)', [user["name"], user["email"], user["team"]])
            for team in teams:
                cursor.execute('INSERT INTO teams (name, members) VALUES (%s, %s)', [team["name"], str(team["members"])])
            for activity in activities:
                cursor.execute('INSERT INTO activities (user, activity, duration) VALUES (%s, %s, %s)', [activity["user"], activity["activity"], activity["duration"]])
            for entry in leaderboard:
                cursor.execute('INSERT INTO leaderboard (team, points) VALUES (%s, %s)', [entry["team"], entry["points"]])
            for workout in workouts:
                cursor.execute('INSERT INTO workouts (name, suggested_for) VALUES (%s, %s)', [workout["name"], workout["suggested_for"]])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
