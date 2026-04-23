from rest_framework import serializers
from .models import CareerPath, UserProfile

class CareerPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPath
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class RecommendationRequestSerializer(serializers.Serializer):
    skills = serializers.CharField(max_length=1000)
    interests = serializers.CharField(max_length=1000)
    experience_level = serializers.ChoiceField(
        choices=['Beginner', 'Intermediate', 'Advanced']
    )
    top_n = serializers.IntegerField(default=5, min_value=1, max_value=10)

class RecommendationResponseSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    required_skills = serializers.CharField()
    recommended_skills = serializers.CharField()
    category = serializers.CharField()
    salary_range = serializers.CharField()
    demand_level = serializers.CharField()
    match_score = serializers.FloatField()