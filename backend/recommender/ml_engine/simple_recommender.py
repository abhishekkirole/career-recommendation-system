import re

class SimpleCareerRecommender:
    def __init__(self):
        self.career_data = None
        self.is_trained = False
    
    def train(self, career_data):
        """Simple training - just load data"""
        self.career_data = career_data
        self.is_trained = True
        print("Simple career recommendation model loaded!")
    
    def calculate_similarity(self, user_text, career_text):
        """Simple text similarity using word overlap"""
        user_words = set(re.findall(r'\w+', user_text.lower()))
        career_words = set(re.findall(r'\w+', career_text.lower()))
        
        if not user_words or not career_words:
            return 0
        
        # Calculate Jaccard similarity
        intersection = user_words.intersection(career_words)
        union = user_words.union(career_words)
        
        return len(intersection) / len(union) if union else 0
    
    def recommend_careers(self, user_skills, user_interests, top_n=5):
        """Generate career recommendations using simple text matching"""
        if not self.is_trained or not self.career_data:
            return []
        
        # Combine user skills and interests
        user_text = user_skills + ' ' + user_interests
        user_text = user_text.lower()
        
        recommendations = []
        
        # Loop through careers (using list of dictionaries)
        for i in range(len(self.career_data['title'])):
            # Combine career text for comparison
            career_text = (
                self.career_data['title'][i] + ' ' + 
                self.career_data['description'][i] + ' ' + 
                self.career_data['required_skills'][i] + ' ' + 
                self.career_data['category'][i]
            ).lower()
            
            # Calculate similarity
            similarity_score = self.calculate_similarity(user_text, career_text)
            
            recommendations.append({
                'title': self.career_data['title'][i],
                'description': self.career_data['description'][i],
                'required_skills': self.career_data['required_skills'][i],
                'recommended_skills': self.career_data['recommended_skills'][i],
                'category': self.career_data['category'][i],
                'salary_range': self.career_data['salary_range'][i],
                'demand_level': self.career_data['demand_level'][i],
                'match_score': round(float(similarity_score) * 100, 2)
            })
        
        # Sort by similarity score and return top N
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        return recommendations[:top_n]
    
    def get_career_data(self):
        """Get the career data"""
        return self.career_data