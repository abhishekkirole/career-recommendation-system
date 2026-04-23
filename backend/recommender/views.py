from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .ml_engine.recommender import CareerRecommender
from .serializers import (
    RecommendationRequestSerializer,
    RecommendationResponseSerializer,
    UserProfileSerializer
)
from .models import UserProfile
import json

# Initialize recommender
recommender = CareerRecommender()


@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({"status": "healthy", "service": "Career Recommendation API"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_recommendations(request):
    """Get career recommendations based on user profile"""
    serializer = RecommendationRequestSerializer(data=request.data)

    if serializer.is_valid():
        try:
            # Train model if not already trained
            if not recommender.is_trained:
                recommender.train()

            # Get recommendations
            recommendations = recommender.recommend_careers(
                user_skills=serializer.validated_data['skills'],
                user_interests=serializer.validated_data['interests'],
                top_n=serializer.validated_data.get('top_n', 5)
            )

            # Save user profile if name and email provided
            if 'name' in request.data and 'email' in request.data:
                user_data = {
                    'name': request.data['name'],
                    'email': request.data['email'],
                    'skills': serializer.validated_data['skills'],
                    'interests': serializer.validated_data['interests'],
                    'experience_level': serializer.validated_data['experience_level']
                }
                user_serializer = UserProfileSerializer(data=user_data)
                if user_serializer.is_valid():
                    user_serializer.save()

            return Response({
                "success": True,
                "recommendations": recommendations,
                "count": len(recommendations)
            })

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_careers(request):
    """Get all available career paths"""
    try:
        if not recommender.is_trained:
            recommender.train()

        from .ml_engine.data_loader import DataLoader
        data_loader = DataLoader()
        career_data = data_loader.load_career_data()

        careers = []
        for i in range(len(career_data['title'])):
            careers.append({
                'title': career_data['title'][i],
                'description': career_data['description'][i],
                'required_skills': career_data['required_skills'][i],
                'category': career_data['category'][i],
                'salary_range': career_data['salary_range'][i],
                'demand_level': career_data['demand_level'][i]
            })

        return Response({
            "success": True,
            "careers": careers,
            "count": len(careers)
        })

    except Exception as e:
        return Response({
            "success": False,
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def register_user(request):
    """Register a new user"""
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')

    if not username or not password:
        return Response(
            {'error': 'Username and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    return Response({
        'success': True,
        'message': f'Account created for {username}!'
    }, status=status.HTTP_201_CREATED)