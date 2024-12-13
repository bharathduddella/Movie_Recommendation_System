class Movie:
    def __init__(self, title, genre, description):
        self.title = title
        self.genre = genre
        self.description = description

    def __str__(self):
        return f"{self.title} ({self.genre}) - {self.description}"
