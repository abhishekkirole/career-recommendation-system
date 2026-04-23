# 🎯 Intelligent Career Recommendation System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange)
![Status](https://img.shields.io/badge/Status-Functional%20Prototype-brightgreen)

*A full-stack web application that provides personalized career recommendations using AI and machine learning*

</div>

## 🚀 Overview

The **Intelligent Career Recommendation System** helps users discover ideal career paths based on their skills, interests, and experience level. Using content-based filtering and natural language processing, the system analyzes user input and matches it with the most suitable careers from a comprehensive database.

## ✨ Features

- **🤖 AI-Powered Recommendations**: Uses TF-IDF and Cosine Similarity for intelligent career matching
- **🎯 Personalized Results**: Tailored recommendations based on individual skills and interests
- **📊 Multiple Career Domains**: Technology, Business, Creative, Healthcare, Education, and more
- **⚡ Real-time Processing**: Instant career matching with detailed analysis
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **🔧 Full-Stack Architecture**: Django backend with modern frontend

## 🛠️ Tech Stack

### Backend
- **Python 3.8+** - Core programming language
- **Django 4.2** - Web framework
- **Django REST Framework** - API development
- **Scikit-learn** - Machine learning algorithms
- **Pandas** - Data processing and analysis

### Frontend
- **HTML5** - Structure and semantics
- **CSS3** - Styling and responsive design
- **JavaScript** - Interactive functionality
- **Modern CSS** - Gradients, animations, and responsive layouts

### Machine Learning
- **TF-IDF Vectorization** - Text processing and feature extraction
- **Cosine Similarity** - Career matching algorithm
- **Content-Based Filtering** - Personalized recommendations

## 📁 Project Structure
career-recommendation-system/
├── backend/ # Django REST API
│ ├── career_recommender/ # Project settings
│ ├── recommender/ # Main app with ML engine
│ ├── manage.py # Django management
│ └── requirements.txt # Python dependencies
├── frontend/ # Web interface
│ ├── career.html # Main recommendation interface
│ ├── new_career.html # Enhanced version
│ └── ai_career.html # AI specialist version
├── README.md # Project documentation
└── .gitignore # Git exclusion rules

text

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
Create virtual environment

bash
python -m venv venv
Activate virtual environment

Windows:

bash
venv\Scripts\activate
macOS/Linux:

bash
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Run database migrations

bash
python manage.py makemigrations
python manage.py migrate
Start the development server

bash
python manage.py runserver
The API will be available at http://localhost:8000

Frontend Setup
Navigate to frontend directory

bash
cd frontend
Open the main interface

Double-click career.html to open in your browser

Or use: python -m http.server 3000 and visit http://localhost:3000/career.html

🎯 How It Works
1. User Input
Users enter their:

Skills (comma-separated): e.g., "Python, JavaScript, Data Analysis"

Interests (comma-separated): e.g., "Technology, Business, Creative"

Experience Level: Beginner, Intermediate, or Advanced

2. Machine Learning Processing
Text Preprocessing: Cleans and normalizes user input

TF-IDF Vectorization: Converts text to numerical representations

Cosine Similarity: Calculates similarity between user profile and career descriptions

3. Recommendation Engine
Content-Based Filtering: Matches user skills with career requirements

Score Calculation: Computes match percentages (0-100%)

Ranking: Sorts careers by relevance and match score

4. Results Display
Career Cards: Detailed information for each recommended career

Match Scores: Visual indicators of relevance

Skill Analysis: Shows which skills matched for each career

📊 ML Model Details
Algorithm: Content-Based Filtering with TF-IDF

Feature Extraction: Text vectorization with n-grams (1-2)

Similarity Metric: Cosine Similarity

Dataset: Custom career database with 25+ professions

Accuracy: High precision in skill-based matching

🌟 Key Features
For Users
✅ Personalized career path discovery

✅ Multiple career domain exploration

✅ Real-time skill analysis

✅ Detailed career information

✅ Mobile-friendly interface

For Developers
✅ Modular Django architecture

✅ RESTful API design

✅ Scalable ML pipeline

✅ Clean, documented code

✅ Easy to extend and customize

🧪 Testing the System
Sample Inputs to Try:
Technology Focused

text
Skills: Python, JavaScript, Machine Learning
Interests: Technology, AI, Web Development
Business Focused

text
Skills: Excel, Communication, Marketing
Interests: Business, Management, Analysis
Creative Focused

text
Skills: Design, Writing, Creativity
Interests: Creative, Marketing, Content
AI Specialist

text
Skills: Python, Machine Learning, Deep Learning, NLP
Interests: Artificial Intelligence, Research
🔧 API Endpoints
GET /api/health/ - Service health check

GET /api/careers/ - List all available careers

POST /api/recommendations/ - Get personalized career recommendations

Example API Request
json
{
  "skills": "Python, JavaScript, Data Analysis",
  "interests": "Technology, Web Development",
  "experienceLevel": "Intermediate"
}
🚀 Deployment
Local Development
Backend: http://localhost:8000

Frontend: Open HTML files directly or use local server

Production Ready
Can be deployed to Heroku, AWS, or DigitalOcean

Database can be upgraded to PostgreSQL

Frontend can be converted to React.js for enhanced functionality

🤝 Contributing
We welcome contributions! Please feel free to:

Fork the repository

Create a feature branch

Make your changes

Submit a pull request

Areas for Contribution
Add more career profiles

Improve ML algorithms

Enhance frontend design

Add user authentication

Implement career progression tracking

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Your Name

GitHub: @yourusername

Portfolio: yourportfolio.com

LinkedIn: Your LinkedIn

🙏 Acknowledgments
Scikit-learn team for excellent ML libraries

Django community for robust web framework

Career data sources and research papers

<div align="center">
⭐ Star this repo if you found it helpful!
"Helping you find the perfect career path through intelligent technology" 🚀

</div> ```