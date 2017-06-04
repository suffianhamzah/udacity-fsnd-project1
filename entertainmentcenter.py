import os
import sys

import media
import fresh_tomatoes
import movieDB_api

spiderman = media.Movie(
    'Spiderman: Homecoming',
    'A new spin on the Super Hero tale, Spiderman',
    'http://assets1.ignimgs.com/2017/03/24/homecoming2-1490383193477_610w.jpg',
    'https://www.youtube.com/watch?v=U0D3AOldjMU')

batman = media.Movie(
    'The Dark Knight',
    'A sequel to "Batman Begins", this continues that story',
    'http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg',
    'https://www.youtube.com/watch?v=EXeTwQWrcwY')

inception = media.Movie(
    'Inception',
    'One of Chris Nolan\'s movie, copied some Anime',
    'http://www.mentalsymmetry.com/forum/wp-content/uploads/2010/09/inception_ver15_xlg.jpg',
    'https://www.youtube.com/watch?v=d3A3-zSOBT4')

HARDCODED_MOVIES = [spiderman, batman, inception]


def get_movies_from_MovieDB(list_type):
    """Obtains movies using the MovieDB api or from the hardcoded list

    Parameters:
      list_type (str): Option that is passed to the MovieDB api to get
                       movie info

    Returns:
      A list containing 20 Movie objects

    Raises:
      KeyError: 'MOVIEDB_API_TOKEN' does not exist
    """
    try:
        api_key = os.environ['MOVIEDB_API_TOKEN']
    except KeyError as error:
        print(error)
        print('You do not have a environment variable called'
              ' "MOVIEDB_API_TOKEN", please set it up by getting one at '
              'https://developers.themoviedb.org.')
        print('Will use hardcoded movie information instead')
        return HARDCODED_MOVIES

    movieDB = movieDB_api.MovieDB(api_key)
    return movieDB.get_movies(list_type)


def main():
    """ Gets the movie list based on the option a user inputs
    Inputs:
      upcoming
      latest
      top_rated
      now_playing
      popular
    if no input is supplied, then the list defaults to popular

    Raises:
      IndexError: No argument is found in the index.
    """
    try:
        option = sys.argv[1]
    except IndexError as error:
        print(error)
        print('no option supplied, defaulting to "popular"')
        option = 'popular'
    print option
    movies = get_movies_from_MovieDB(option)

    # We call the open_movies_page method and pass in the list of movies
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
