from flask import Flask, render_template, request
from recommendation_engine import RecommendationEngine

# Initialize Flask app
app = Flask(__name__)

# Initialize Recommendation Engine
engine = RecommendationEngine("data/movies.csv")

@app.route("/")
def home():
    """Render the home page with the input form."""
    return render_template("home.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    """Handle user input and display recommendations."""
    movie_title = request.form.get("movie_title")
    if not movie_title:
        return render_template("home.html", error="Please enter a movie title.")
    
    try:
        recommendations = engine.get_recommendations(movie_title)
        return render_template("results.html", movie_title=movie_title, recommendations=recommendations)
    except Exception as e:
        return render_template("home.html", error=f"Error: {str(e)}. Make sure the movie exists in our dataset.")

if __name__ == "__main__":
    app.run(debug=True)
