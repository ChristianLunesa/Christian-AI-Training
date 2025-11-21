
from django.core.management.base import BaseCommand
from octofit_tracker.api.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel_team = Team.objects.create(name="Marvel")
        dc_team = Team.objects.create(name="DC")

        # Create Users
        marvel_users = [
            User.objects.create(username="Iron Man", email="ironman@marvel.com", first_name="Tony", last_name="Stark"),
            User.objects.create(username="Captain America", email="cap@marvel.com", first_name="Steve", last_name="Rogers"),
            User.objects.create(username="Thor", email="thor@marvel.com", first_name="Thor", last_name="Odinson"),
            User.objects.create(username="Black Widow", email="widow@marvel.com", first_name="Natasha", last_name="Romanoff"),
        ]
        dc_users = [
            User.objects.create(username="Superman", email="superman@dc.com", first_name="Clark", last_name="Kent"),
            User.objects.create(username="Batman", email="batman@dc.com", first_name="Bruce", last_name="Wayne"),
            User.objects.create(username="Wonder Woman", email="wonderwoman@dc.com", first_name="Diana", last_name="Prince"),
            User.objects.create(username="Flash", email="flash@dc.com", first_name="Barry", last_name="Allen"),
        ]

        # Assign members to teams
        marvel_team.members.set(marvel_users)
        dc_team.members.set(dc_users)

        # Create Activities
        Activity.objects.create(user=marvel_users[0], type="Running", duration=30, calories=300, date="2025-11-21T08:00:00Z")
        Activity.objects.create(user=dc_users[1], type="Cycling", duration=45, calories=400, date="2025-11-21T09:00:00Z")
        Activity.objects.create(user=dc_users[2], type="Swimming", duration=60, calories=500, date="2025-11-21T10:00:00Z")
        Activity.objects.create(user=dc_users[3], type="Sprinting", duration=20, calories=250, date="2025-11-21T11:00:00Z")

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel_team, points=120, week=1)
        Leaderboard.objects.create(team=dc_team, points=110, week=1)

        # Create Workouts
        Workout.objects.create(name="Weightlifting", description="Heavy weights", difficulty="Hard", duration=60)
        Workout.objects.create(name="Pushups", description="Bodyweight exercise", difficulty="Medium", duration=30)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data using Django ORM.'))
