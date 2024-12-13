from recommendation_engine import RecommendationEngine

def main():
    print("=== Movie Recommendation System ===")
    
    # Initialize Recommendation Engine
    dataset_path = "data/movies.csv"
    engine = RecommendationEngine(dataset_path)
    
    # Prompt user for input
    while True:
        movie_title = input("\nEnter a movie title (or 'exit' to quit): ").strip()
        if movie_title.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            recommendations = engine.get_recommendations(movie_title)
            print(f"\nRecommendations for '{movie_title}':")
            for idx, rec in enumerate(recommendations, start=1):
                print(f"{idx}. {rec['title']} ({rec['genre']}) - {rec['description']}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
