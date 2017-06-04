import requests

from media import Movie


class MovieDB():
    """A class for accessing the MovieDB API

    This class provides a way to get the latest, popular or top-rated
    movie list using the MovieDB API

    API Docs: https://developers.themoviedb.org

    Attributes:
        api_key (str): api_key needed to access the MovieDB API
        BASE_URL (str): base url for accessing the MovieDB API
        language (str): language for the movie details. Default = 'en-US'
        IMAGE_URL (str): base_url for getting movie images including
                         backdrop and poster path
    """

    def __init__(self, api_key):
        """Inits the class with the API_Key, API urls and language."""
        self.api_key = api_key
        self.BASE_URL = 'https://api.themoviedb.org/3/movie/'
        self.language = 'en-US'
        self.IMAGE_URL = 'https://image.tmdb.org/t/p/w500'

    def get_movies(self, list_type='latest', num_pages=1):
        """Gets a list of movies using the API

        This function takes in a list_type (str), which defaults to 'latest'
        Possible types: ['latest', 'popular','now_playing','upcoming']

        Parameters:
            list_type (str): A string that specificies movie list type
            num_pages (int): Will affect the number of movie items returned

        Returns:
            A list containing 20 items of latest Movie Objects IF
            type and num_pages are not specified.
        """

        payload = {
            'api_key': self.api_key,
            'language': self.language,
            'pages': 1
        }

        url = self.BASE_URL + list_type
        movie_results = []
        resp = requests.get(url, params=payload)
        # We convert the JSON object into a Python Dict, and save 'results'
        movie_results = resp.json()['results']  # list of movie objects

        if num_pages > 1:
            for i in range(2, num_pages + 1):
                payload['pages'] = i
                resp = requests.get(url, params=payload)
                movie_results.extend(resp.json()['results'])

        converted_movies = [self._convert_to_Movie(movie)
                            for movie in movie_results]
        return converted_movies

    def _convert_to_Movie(self, MovieDB):
        """Converts MovieDB movie object to our Movie object

        This is a private method for trimming the MovieDB object
        returned by the API into a Movie object defined in ./media.py

        Parameters:
          movie_list (list:dicts): Contains a list of movie dictionaries
                                   returned by the MovieDB API

        Returns:
          A list of movie objects. title and overview are encoded to handle
          unicode characters.
        """
        return Movie(MovieDB['original_title'].encode('utf-8'),
                     MovieDB['overview'].encode('utf-8'),
                     self._get_image_url(MovieDB['poster_path']),
                     self._get_trailer_url(MovieDB['id']))

    def _get_image_url(self, image_filepath):
        """Returns an image url based on the filepath given"""
        return self.IMAGE_URL + image_filepath

    def _get_trailer_url(self, movie_id):
        """Returns a youtube url trailer based on the movie_id

        Parameters:
            movie_id (int) : IMDB movie id obtained from the MovieDB object

        Returns:
            A youtube movie_url if found. If not, a placeholder url will be
            used.

        Raises:
            Requests.exception Error
        """
        payload = {
            'api_key': self.api_key,
            'language': self.language
        }

        youtube_base_url = 'https://www.youtube.com/watch?v='
        url = self.BASE_URL + str(movie_id) + '/videos'
        resp = requests.get(url, params=payload)

        if resp.status_code == requests.codes.ok:
            video_results = resp.json()['results']
            for video in video_results:
                if video['type'] == u'Trailer':
                    return youtube_base_url + video['key']

            print 'Couldnt find a trailer for the movie, returning placeholder'
            print 'video trailer.'
            return 'https://www.youtube.com/watch?v=FnCdOQsX5kc'
        else:
            # Throws an error if the movie_id is not illegible
            resp.raise_for_status()
