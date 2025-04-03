import os
import praw
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # NEW

# Load API credentials from .env
load_dotenv()

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()  # NEW

# Flask app
app = Flask(__name__)

def analyze_sentiment(text):
    """Perform sentiment analysis using VADER with refined thresholds"""
    sentiment_score = analyzer.polarity_scores(text)["compound"]

    # Adjust thresholds for better accuracy
    if sentiment_score >= 0.2:
        return "Positive 😊"
    elif sentiment_score <= -0.2:
        return "Negative 😡"
    else:
        return "Neutral 😐"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fetch_reddit", methods=["GET"])
def fetch_reddit():
    """Fetch top 10 Reddit posts from a user-specified subreddit"""
    topic = request.args.get("topic", "worldnews")  # Default to 'worldnews'
    subreddit = reddit.subreddit(topic)
    posts = [{"title": post.title, "sentiment": analyze_sentiment(post.title)} for post in subreddit.hot(limit=10)]
    return jsonify(posts)

if __name__ == "__main__":
    app.run(debug=True)
