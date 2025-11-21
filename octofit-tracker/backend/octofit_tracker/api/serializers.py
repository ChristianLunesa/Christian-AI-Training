from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    team = serializers.CharField(max_length=50)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    members = serializers.ListField(child=serializers.CharField(max_length=100))

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    activity = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    team = serializers.CharField(max_length=50)
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    workout = serializers.CharField(max_length=100)
    reps = serializers.IntegerField()
