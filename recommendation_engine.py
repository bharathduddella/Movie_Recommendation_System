import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    def __init__(self, dataset_path):
        self.movies_df = pd.read_csv(dataset_path)
        self.tfidf_matrix = None

    def preprocess(self):
        """Combine genre and description into a single feature and vectorize."""
        self.movies_df['combined_features'] = self.movies_df['genre'] + " " + self.movies_df['description']
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.movies_df['combined_features'])

    def get_recommendations(self, title, top_n=5):
        """Generate recommendations based on cosine similarity."""
        if self.tfidf_matrix is None:
            self.preprocess()

        try:
            # Find the index of the movie
            idx = self.movies_df[self.movies_df['title'].str.contains(title, case=False, na=False)].index[0]
        except IndexError:
            raise ValueError(f"Movie '{title}' not found in the dataset.")

        # Compute cosine similarity
        cosine_sim = cosine_similarity(self.tfidf_matrix[idx], self.tfidf_matrix).flatten()
        # Get indices of top N similar movies
        similar_indices = cosine_sim.argsort()[-top_n-1:-1][::-1]
        return self.movies_df.iloc[similar_indices][['title', 'genre', 'description']].to_dict(orient='records')
