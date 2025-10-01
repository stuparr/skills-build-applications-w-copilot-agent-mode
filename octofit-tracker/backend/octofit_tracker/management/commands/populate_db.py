from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')
        
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create teams
        teams = [
            Team(name='Iron Warriors', description='The strongest team'),
            Team(name='Speed Demons', description='Fastest runners in the school'),
            Team(name='Yoga Masters', description='Flexibility and mindfulness experts'),
        ]
        Team.objects.bulk_create(teams)
        self.stdout.write(self.style.SUCCESS(f'Created {len(teams)} teams'))
        
        # Create users
        users = [
            User(name='Alice Johnson', email='alice@example.com', team='Iron Warriors'),
            User(name='Bob Smith', email='bob@example.com', team='Speed Demons'),
            User(name='Charlie Brown', email='charlie@example.com', team='Iron Warriors'),
            User(name='Diana Prince', email='diana@example.com', team='Yoga Masters'),
            User(name='Ethan Hunt', email='ethan@example.com', team='Speed Demons'),
        ]
        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'Created {len(users)} users'))
        
        # Create activities
        activities = [
            Activity(user='Alice Johnson', activity='Running', duration=30),
            Activity(user='Alice Johnson', activity='Weight Training', duration=45),
            Activity(user='Bob Smith', activity='Running', duration=60),
            Activity(user='Charlie Brown', activity='Weight Training', duration=50),
            Activity(user='Diana Prince', activity='Yoga', duration=40),
            Activity(user='Ethan Hunt', activity='Running', duration=45),
            Activity(user='Bob Smith', activity='Cycling', duration=90),
            Activity(user='Diana Prince', activity='Pilates', duration=35),
        ]
        Activity.objects.bulk_create(activities)
        self.stdout.write(self.style.SUCCESS(f'Created {len(activities)} activities'))
        
        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user='Bob Smith', team='Speed Demons', total_minutes=150, rank=1),
            Leaderboard(user='Charlie Brown', team='Iron Warriors', total_minutes=95, rank=2),
            Leaderboard(user='Alice Johnson', team='Iron Warriors', total_minutes=75, rank=3),
            Leaderboard(user='Diana Prince', team='Yoga Masters', total_minutes=75, rank=4),
            Leaderboard(user='Ethan Hunt', team='Speed Demons', total_minutes=45, rank=5),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)
        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_entries)} leaderboard entries'))
        
        # Create workouts
        workouts = [
            Workout(
                name='Morning Cardio',
                description='A quick cardio session to start your day',
                duration=20,
                difficulty='beginner',
                suggested_for='All fitness levels'
            ),
            Workout(
                name='Strength Training',
                description='Build muscle with this comprehensive workout',
                duration=45,
                difficulty='intermediate',
                suggested_for='Those looking to build strength'
            ),
            Workout(
                name='HIIT Blast',
                description='High intensity interval training for maximum results',
                duration=30,
                difficulty='advanced',
                suggested_for='Experienced athletes'
            ),
            Workout(
                name='Yoga Flow',
                description='Relax and stretch with this gentle yoga routine',
                duration=40,
                difficulty='beginner',
                suggested_for='Anyone seeking flexibility and mindfulness'
            ),
        ]
        Workout.objects.bulk_create(workouts)
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workouts'))
        
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
