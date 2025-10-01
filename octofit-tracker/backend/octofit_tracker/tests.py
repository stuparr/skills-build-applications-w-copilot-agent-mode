from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test User", email="test@example.com", team="marvel")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.team, "marvel")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="marvel", members=["Iron Man", "Thor"])
        self.assertEqual(team.name, "marvel")
        self.assertIn("Thor", team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="Iron Man", activity="Running", duration=30)
        self.assertEqual(activity.activity, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team="marvel", points=100)
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Push Ups", suggested_for="Iron Man")
        self.assertEqual(workout.name, "Push Ups")
