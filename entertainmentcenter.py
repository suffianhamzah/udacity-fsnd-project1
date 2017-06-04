import media
import fresh_tomatoes

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
    'https://www.youtube.com/watch?v=YoHD9XEInc0',
    'https://www.youtube.com/watch?v=d3A3-zSOBT4')

movies = [spiderman, batman, inception]

fresh_tomatoes.open_movies_page(movies)