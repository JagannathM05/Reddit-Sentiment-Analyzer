# Reddit Sentiment Analyzer 🔍🧠

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

A real-time sentiment analysis tool that evaluates the emotional tone of Reddit post titles using Natural Language Processing (NLP).

## 🌟 Features

- *Subreddit Analysis*: Fetch top posts from any Reddit community
- *Sentiment Scoring*: VADER-powered sentiment classification (Positive/Negative/Neutral)
- *Visual Feedback*: Emoji indicators (😊/😡/😐) for quick sentiment recognition
- *Responsive UI*: Clean, mobile-friendly interface
- *Real-time Results*: Instant analysis with no page reloads
- *Custom Thresholds*: Optimized sentiment classification boundaries


## 🖥 Usage
Launch the app and visit http://localhost:5000

Enter a subreddit name (e.g., "worldnews", "technology", "funny")

View sentiment analysis results for the top 10 posts

Demo Screenshot

##   Sentiment Analysis Methodology
The system uses VADER (Valence Aware Dictionary and sEntiment Reasoner) with customized thresholds:

Sentiment	Compound Score Range	Emoji
Positive	≥ 0.2	😊
Negative	≤ -0.2	😡
Neutral	-0.2 < score < 0.2	😐
VADER is particularly effective for social media text because it:

Handles slang and emoticons

Understands degree modifiers ("very good" vs "good")

Doesn't require training data

## 🏗 Project Structure
Copy
Reddit-Sentiment-Analyzer/
├── app.py                 # Main application logic
├── requirements.txt       # Dependency list
├── .gitignore            # Git ignore rules
├── static/
│   └── style.css          # Stylesheet
└── templates/
    └── index.html         # Frontend interface
## 🌐 API Endpoints
GET / - Main application interface

GET /fetch_reddit?topic=<subreddit> - Returns JSON with posts and sentiment analysis

## 🛠 Technologies Used
Python 3

Flask (Web Framework)

PRAW (Python Reddit API Wrapper)

VADER Sentiment Analysis

HTML5, CSS3, JavaScript

Render (for deployment)

## 🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements
PRAW library for Reddit API access

VADER sentiment analysis tool

Flask microframework

Render for hosting the demo

Happy analyzing! Discover the emotional pulse of Reddit communities! 🚀
