from django.db import models

class CareerPath(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.TextField(help_text="Comma-separated skills")
    recommended_skills = models.TextField(help_text="Comma-separated skills")
    salary_range = models.CharField(max_length=100)
    demand_level = models.CharField(max_length=50, choices=[
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ])
    category = models.CharField(max_length=100)
    
    def get_skills_list(self):
        return [skill.strip() for skill in self.required_skills.split(',')]
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    skills = models.TextField(help_text="Comma-separated skills")
    interests = models.TextField(help_text="Comma-separated interests")
    experience_level = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_skills_list(self):
        return [skill.strip() for skill in self.skills.split(',')]
    
    def get_interests_list(self):
        return [interest.strip() for interest in self.interests.split(',')]