from .data_loader import DataLoader
from .simple_recommender import SimpleCareerRecommender

class CareerRecommender:
    def __init__(self):
        self.data_loader = DataLoader()
        self.simple_recommender = SimpleCareerRecommender()
        self.is_trained = False
    
    def train(self):
        """Train the recommendation model"""
        career_data = self.data_loader.load_career_data()
        self.simple_recommender.train(career_data)
        self.is_trained = True
        print("Career recommendation model trained successfully!")
    
    def recommend_careers(self, user_skills, user_interests, top_n=5):
        """Generate career recommendations based on user profile"""
        if not self.is_trained:
            self.train()
        
        return self.simple_recommender.recommend_careers(user_skills, user_interests, top_n)