import webbrowser


class Movie:
    """The Movie that is exhibited at the site"""

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
        """Inits Movie with title, storyline, poster image and
        trailer video."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the movie trailer on browser"""
        webbrowser.open(self.trailer_youtube_url)
