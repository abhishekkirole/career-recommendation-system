# 🎯 Intelligent Career Recommendation System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?style=for-the-badge&logo=django)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange?style=for-the-badge&logo=scikit-learn)
![JWT](https://img.shields.io/badge/Auth-JWT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

*A full-stack AI-powered web application that provides personalized career recommendations using Machine Learning*

[🚀 Live Demo](#) • [📡 API Docs](#-api-endpoints) • [🛠️ Setup](#-quick-start)

</div>

---

## 📌 Overview

The **Intelligent Career Recommendation System** helps users discover ideal career paths based on their skills, interests, and experience level. Using **content-based filtering** and **natural language processing**, the system analyzes user input and matches it with the most suitable careers from a comprehensive database of 25+ professions.

---

## ✨ Features

- 🤖 **AI-Powered Recommendations** — TF-IDF + Cosine Similarity for intelligent career matching
- 🎯 **Personalized Results** — Tailored to individual skills, interests & experience level
- 📊 **10+ Career Domains** — Technology, Business, Creative, Healthcare, Education & more
- ⚡ **Real-time Processing** — Instant career matching with match score percentages
- 🔐 **User Authentication** — JWT-based secure login & registration
- 📱 **Responsive Design** — Works seamlessly on desktop and mobile
- 🔧 **Full-Stack Architecture** — Django REST API + React.js frontend

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React.js 18, CSS3, JavaScript (ES6+) |
| **Backend** | Python 3.8+, Django 6.0, Django REST Framework |
| **Machine Learning** | Scikit-learn, TF-IDF Vectorization, Cosine Similarity, Pandas |
| **Authentication** | JWT (djangorestframework-simplejwt) |
| **Database** | SQLite (development) / PostgreSQL (production) |
| **API** | RESTful API with CORS support |

---

## 📁 Project Structure

```
career-recommendation-system/
├── backend/
│   ├── career_recommender/        # Django project settings
│   │   ├── settings.py
│   │   └── urls.py
│   ├── recommender/               # Main app
│   │   ├── ml_engine/             # ML recommendation engine
│   │   │   ├── recommender.py     # TF-IDF + Cosine Similarity
│   │   │   └── data_loader.py     # Career database
│   │   ├── models.py              # CareerPath, UserProfile models
│   │   ├── views.py               # API views
│   │   ├── serializers.py         # DRF serializers
│   │   └── urls.py                # API routes
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js                 # Main React component + Auth
│   │   ├── App.css                # Styling
│   │   └── index.js
│   └── package.json
└── README.md
```

---


## 🎯 How It Works

```
User Registers / Logs In (JWT Auth)
           ↓
  Enters Skills + Interests + Experience
           ↓
    Text Preprocessing & Cleaning
           ↓
      TF-IDF Vectorization
           ↓
    Cosine Similarity Calculation
           ↓
  Ranked Career Recommendations
    with Match Score (0-100%)
```

1. **Authentication** — User registers/logs in via JWT tokens
2. **User Input** — Skills, interests, and experience level
3. **TF-IDF Vectorization** — Converts text to numerical vectors
4. **Cosine Similarity** — Measures match between user profile and careers
5. **Ranked Results** — Returns top 5 careers with match percentages

---

## 📡 API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `GET` | `/api/health/` | ❌ | Service health check |
| `GET` | `/api/careers/` | ❌ | List all career paths |
| `POST` | `/api/recommendations/` | ✅ | Get personalized recommendations |
| `POST` | `/api/auth/register/` | ❌ | Register new user |
| `POST` | `/api/auth/login/` | ❌ | Login & get JWT token |
| `POST` | `/api/auth/refresh/` | ❌ | Refresh JWT token |

### Example Request

```json
POST /api/recommendations/
Authorization: Bearer <jwt_token>

{
  "skills": "Python, Machine Learning, Data Analysis",
  "interests": "AI, Web Development",
  "experience_level": "Intermediate"
}
```

### Example Response

```json
{
  "success": true,
  "recommendations": [
    {
      "title": "Data Scientist",
      "match_score": 92.5,
      "description": "Extract insights from complex data using ML algorithms",
      "category": "Data & Analytics",
      "salary_range": "$90,000 - $150,000",
      "demand_level": "High",
      "required_skills": "Python, Machine Learning, Statistics, SQL",
      "recommended_skills": "Deep Learning, Spark, Tableau"
    }
  ],
  "count": 5
}
```

---

## 🧪 Sample Inputs to Try

**Technology / AI:**
```
Skills: Python, Machine Learning, Deep Learning
Interests: Artificial Intelligence, Research
Experience: Intermediate
```

**Web Development:**
```
Skills: JavaScript, React, HTML, CSS
Interests: Web Development, Design
Experience: Beginner
```

**Business / Management:**
```
Skills: Excel, Communication, Marketing
Interests: Business, Management, Analysis
Experience: Advanced
```

---

## 📊 ML Model Details

| Property | Value |
|---|---|
| Algorithm | Content-Based Filtering |
| Feature Extraction | TF-IDF with n-grams (1-2) |
| Similarity Metric | Cosine Similarity |
| Career Database | 25+ professions |
| Response Time | < 500ms |

---

## 👨‍💻 Author

**Abhishek Kirole**

[![GitHub](https://img.shields.io/badge/GitHub-@abhishekirole-black?style=flat&logo=github)](https://github.com/abhishekirole)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abhishek%20Kirole-blue?style=flat&logo=linkedin)](https://linkedin.com/in/abhishek-kirole)
[![Email](https://img.shields.io/badge/Email-abhishekkirole7@gmail.com-red?style=flat&logo=gmail)](mailto:abhishekkirole77@gmail.com)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- Scikit-learn team for excellent ML libraries
- Django community for the robust web framework
- React.js community for the frontend framework

---

<div align="center">

⭐ **Star this repo if you found it helpful!**

*"Helping you find the perfect career path through intelligent technology"* 🚀

</div>
