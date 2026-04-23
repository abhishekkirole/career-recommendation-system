import re

class TextPreprocessor:
    def __init__(self):
        pass
    
    def clean_text(self, text):
        """Clean and preprocess text"""
        if not text:
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text
    
    def prepare_career_data(self, career_data):
        """Prepare career data for processing"""
        # Since we're using simple matching, just return the data
        return career_data
    
    def fit_vectorizer(self, documents):
        """Dummy method for compatibility"""
        pass
    
    def transform_text(self, documents):
        """Dummy method for compatibility"""
        return documents