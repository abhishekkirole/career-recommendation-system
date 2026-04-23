import os
from django.conf import settings

class DataLoader:
    def __init__(self):
        self.data_path = os.path.join(settings.BASE_DIR, 'data', 'career_data.csv')
    
    def load_career_data(self):
        """Load career data from CSV or create sample data"""
        try:
            # For now, we'll just return sample data
            return self._create_sample_data()
        except Exception as e:
            print(f"Error loading data: {e}")
            return self._create_sample_data()
    
    def _create_sample_data(self):
        """Create sample career data"""
        sample_data = {
            'title': [
                'Data Scientist',
                'Frontend Developer', 
                'Backend Developer',
                'DevOps Engineer',
                'Machine Learning Engineer',
                'Data Analyst',
                'UX/UI Designer',
                'Product Manager',
                'Cloud Architect',
                'Cybersecurity Analyst'
            ],
            'description': [
                'Extract insights from complex data using ML algorithms',
                'Build user-facing web applications and interfaces',
                'Develop server-side logic and database architecture',
                'Manage deployment, scaling, and infrastructure',
                'Design and implement ML models and systems',
                'Analyze data to support business decisions',
                'Create user-centered digital experiences',
                'Lead product development and strategy',
                'Design and implement cloud solutions',
                'Protect systems and networks from cyber threats'
            ],
            'required_skills': [
                'Python, Machine Learning, Statistics, SQL, Data Visualization',
                'JavaScript, HTML, CSS, React, TypeScript',
                'Python, Java, SQL, APIs, Database Design',
                'Docker, Kubernetes, AWS, CI/CD, Linux',
                'Python, TensorFlow, Deep Learning, ML Algorithms',
                'SQL, Excel, Statistics, Data Visualization, Python',
                'Figma, User Research, Wireframing, Prototyping',
                'Product Strategy, Agile, User Stories, Roadmapping',
                'AWS, Azure, Cloud Security, Networking, Terraform',
                'Network Security, Ethical Hacking, SIEM, Firewalls'
            ],
            'recommended_skills': [
                'Deep Learning, Big Data, Cloud Computing, Business Acumen',
                'Vue.js, SASS, Webpack, Testing, Accessibility',
                'Microservices, Caching, Security, System Design',
                'Monitoring, Scripting, Infrastructure as Code',
                'PyTorch, MLOps, Computer Vision, NLP',
                'Tableau, Power BI, A/B Testing, Storytelling',
                'Interaction Design, UX Research, Design Systems',
                'Data Analysis, Market Research, Leadership',
                'Kubernetes, Serverless, Cost Optimization',
                'Incident Response, Threat Intelligence, Compliance'
            ],
            'category': [
                'Data & Analytics', 'Web Development', 'Web Development',
                'Infrastructure', 'AI/ML', 'Data & Analytics', 'Design',
                'Management', 'Infrastructure', 'Security'
            ],
            'salary_range': [
                '$90,000 - $150,000', '$70,000 - $130,000', '$75,000 - $140,000',
                '$85,000 - $145,000', '$95,000 - $160,000', '$65,000 - $120,000',
                '$60,000 - $110,000', '$80,000 - $150,000', '$100,000 - $170,000',
                '$75,000 - $140,000'
            ],
            'demand_level': [
                'High', 'High', 'High', 'High', 'High', 'Medium', 'High',
                'High', 'High', 'High'
            ]
        }
        
        # We'll use a simple dictionary approach since pandas might not be installed
        return sample_data