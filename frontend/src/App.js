import React, { useState } from 'react';
import './App.css';

// ==================== AUTH COMPONENT ====================
function Auth({ onLogin }) {
  const [isLogin, setIsLogin] = useState(true);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    email: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      if (isLogin) {
        const response = await fetch('http://localhost:8000/api/auth/login/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: formData.username,
            password: formData.password
          })
        });
        const data = await response.json();
        if (data.access) {
          localStorage.setItem('token', data.access);
          localStorage.setItem('username', formData.username);
          onLogin(formData.username);
        } else {
          alert('Login failed: ' + (data.detail || 'Invalid credentials'));
        }
      } else {
        const response = await fetch('http://localhost:8000/api/auth/register/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        });
        const data = await response.json();
        if (data.success) {
          alert('Account created successfully! Please login.');
          setIsLogin(true);
        } else {
          alert('Error: ' + data.error);
        }
      }
    } catch (error) {
      alert('Connection error: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={authStyles.container}>
      <div style={authStyles.card}>
        <h1 style={authStyles.title}>🎯 Career Recommender</h1>
        <p style={authStyles.subtitle}>Discover your perfect career path using AI</p>

        <div style={authStyles.tabs}>
          <button
            style={isLogin ? authStyles.activeTab : authStyles.tab}
            onClick={() => setIsLogin(true)}
          >
            Login
          </button>
          <button
            style={!isLogin ? authStyles.activeTab : authStyles.tab}
            onClick={() => setIsLogin(false)}
          >
            Sign Up
          </button>
        </div>

        <form onSubmit={handleSubmit} style={authStyles.form}>
          <input
            style={authStyles.input}
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
            required
          />
          {!isLogin && (
            <input
              style={authStyles.input}
              type="email"
              name="email"
              placeholder="Email (optional)"
              value={formData.email}
              onChange={handleChange}
            />
          )}
          <input
            style={authStyles.input}
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <button style={authStyles.button} type="submit" disabled={loading}>
            {loading ? 'Please wait...' : isLogin ? '🔐 Login' : '✅ Create Account'}
          </button>
        </form>

        <p style={authStyles.switchText}>
          {isLogin ? "Don't have an account? " : "Already have an account? "}
          <span style={authStyles.link} onClick={() => setIsLogin(!isLogin)}>
            {isLogin ? 'Sign Up' : 'Login'}
          </span>
        </p>
      </div>
    </div>
  );
}

const authStyles = {
  container: {
    minHeight: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
  },
  card: {
    background: 'white',
    borderRadius: '16px',
    padding: '40px',
    width: '100%',
    maxWidth: '400px',
    boxShadow: '0 20px 60px rgba(0,0,0,0.2)',
  },
  title: { textAlign: 'center', color: '#333', marginBottom: '8px' },
  subtitle: { textAlign: 'center', color: '#666', marginBottom: '24px', fontSize: '14px' },
  tabs: {
    display: 'flex',
    marginBottom: '24px',
    borderRadius: '8px',
    overflow: 'hidden',
    border: '1px solid #ddd',
  },
  tab: {
    flex: 1, padding: '10px', border: 'none',
    background: '#f5f5f5', cursor: 'pointer', fontSize: '14px',
  },
  activeTab: {
    flex: 1, padding: '10px', border: 'none',
    background: '#667eea', color: 'white',
    cursor: 'pointer', fontSize: '14px', fontWeight: 'bold',
  },
  form: { display: 'flex', flexDirection: 'column', gap: '16px' },
  input: {
    padding: '12px 16px', borderRadius: '8px',
    border: '1px solid #ddd', fontSize: '14px', outline: 'none',
  },
  button: {
    padding: '12px', borderRadius: '8px', border: 'none',
    background: 'linear-gradient(135deg, #667eea, #764ba2)',
    color: 'white', fontSize: '16px', fontWeight: 'bold',
    cursor: 'pointer', marginTop: '8px',
  },
  switchText: { textAlign: 'center', marginTop: '20px', color: '#666', fontSize: '14px' },
  link: { color: '#667eea', cursor: 'pointer', fontWeight: 'bold' },
};

// ==================== MAIN APP COMPONENT ====================
function App() {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [user, setUser] = useState(localStorage.getItem('username'));
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    skills: '',
    interests: '',
    experience_level: 'Beginner'
  });

  const handleLogin = (username) => {
    setUser(username);
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    setUser(null);
    setRecommendations([]);
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/recommendations/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (data.success) {
        setRecommendations(data.recommendations);
      } else {
        alert('Error: ' + (data.error || JSON.stringify(data)));
      }
    } catch (error) {
      alert('Error connecting to server: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  // Show Auth page if not logged in
  if (!user) {
    return <Auth onLogin={handleLogin} />;
  }

  return (
    <div className="App">
      <header className="header">
        <h1>Intelligent Career Recommendation System</h1>
        <p>Discover your ideal career path based on your skills and interests</p>
        <div style={{ marginTop: '12px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '12px' }}>
          <span style={{ color: 'white', fontSize: '15px' }}>👋 Welcome, <strong>{user}</strong>!</span>
          <button
            onClick={handleLogout}
            style={{
              padding: '6px 16px', borderRadius: '6px',
              border: '2px solid white', background: 'transparent',
              color: 'white', cursor: 'pointer', fontSize: '13px',
              fontWeight: 'bold'
            }}
          >
            🚪 Logout
          </button>
        </div>
      </header>

      <main className="main">
        <div className="form-container">
          <h2>Find Your Perfect Career Path</h2>
          <form onSubmit={handleSubmit} className="form">
            <div className="form-group">
              <label>Name:</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="Enter your name"
              />
            </div>

            <div className="form-group">
              <label>Email:</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="Enter your email"
              />
            </div>

            <div className="form-group">
              <label>Skills (comma-separated):</label>
              <textarea
                name="skills"
                value={formData.skills}
                onChange={handleChange}
                placeholder="e.g., Python, JavaScript, Data Analysis, Machine Learning"
                rows="3"
                required
              />
            </div>

            <div className="form-group">
              <label>Interests (comma-separated):</label>
              <textarea
                name="interests"
                value={formData.interests}
                onChange={handleChange}
                placeholder="e.g., Web Development, Data Science, AI, UX Design"
                rows="3"
                required
              />
            </div>

            <div className="form-group">
              <label>Experience Level:</label>
              <select
                name="experience_level"
                value={formData.experience_level}
                onChange={handleChange}
              >
                <option value="Beginner">Beginner (0-2 years)</option>
                <option value="Intermediate">Intermediate (2-5 years)</option>
                <option value="Advanced">Advanced (5+ years)</option>
              </select>
            </div>

            <button type="submit" disabled={loading}>
              {loading ? 'Finding Recommendations...' : 'Get Career Recommendations'}
            </button>
          </form>
        </div>

        {recommendations.length > 0 && (
          <div className="results-container">
            <h2>Your Career Recommendations</h2>
            <div className="results-grid">
              {recommendations.map((career, index) => (
                <div key={index} className="career-card">
                  <div className="card-header">
                    <h3>{career.title}</h3>
                    <div className="match-score">{career.match_score}% Match</div>
                  </div>

                  <div className="card-body">
                    <p className="description">{career.description}</p>

                    <div className="details">
                      <div className="detail-item">
                        <strong>Category:</strong> {career.category}
                      </div>
                      <div className="detail-item">
                        <strong>Salary Range:</strong> {career.salary_range}
                      </div>
                      <div className="detail-item">
                        <strong>Demand:</strong>
                        <span className={`demand-level ${career.demand_level.toLowerCase()}`}>
                          {career.demand_level}
                        </span>
                      </div>
                    </div>

                    <div className="skills-section">
                      <div className="skills-group">
                        <strong>Required Skills:</strong>
                        <div className="skills-list">
                          {career.required_skills.split(',').map((skill, idx) => (
                            <span key={idx} className="skill-tag">{skill.trim()}</span>
                          ))}
                        </div>
                      </div>

                      <div className="skills-group">
                        <strong>Recommended Skills:</strong>
                        <div className="skills-list">
                          {career.recommended_skills.split(',').map((skill, idx) => (
                            <span key={idx} className="skill-tag">{skill.trim()}</span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      <footer className="footer">
        <p>Career Recommendation System &copy; 2024</p>
      </footer>
    </div>
  );
}

export default App;