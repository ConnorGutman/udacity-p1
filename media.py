# Import necessary dependencies such as webbrowser
import webbrowser

# Create a class called Movie which will contain relevant information
# about films


class Movie():
    """This class provides a way to store movie information"""
    # Create the initializer for the Movie class. This will declare several
    # variables shown bellow such as title, storyline, etc.

    def __init__(self,
                 movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Create a function called show_trailer which opens a movie's trailer in
    # your web browser.

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
