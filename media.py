import webbrowser

class Movie():

    """
    The movie object is initialized below.
    title:
        the title of the movie
    poster_image_url:
        fully qualifed url of the cover art of the movie
        ex. "https://www.google.com/images/moviecover.png"
    trailer_youtube_url:
        movie trailer youtube link
        ex. "https://www.youtube.com/watch?v=u_32ujdsdjas"
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
