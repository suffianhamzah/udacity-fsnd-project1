import webbrowser


class Movie():
    """Represents a Movie and its attributes

    Attribute:
    title               (str): Title of the movie
    storyline           (str): Storyline of the movie
    poster_image_url    (str): Poster image link of the movie
    youtube_trailer_url (str): Youtube trailer URL for the movie
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, youtube_trailer):
        """Inits Movie with its attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        """Opens a browser with the object's youtube link"""
        webbrowser.open(self.trailer_youtube_url)
