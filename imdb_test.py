import imdb


def test_imdbpy():
    ia = imdb.IMDb()
    try:
        # Attempt to retrieve information for "The Shawshank Redemption"
        movie = ia.search_movie('The Shawshank Redemption')[0]
        ia.update(movie)
        title = movie.get('title', 'N/A')
        rating = movie.get('rating', 'N/A')
        year = movie.get('year', 'N/A')
        directors = movie.get('directors')
        director = directors[0]['name'] if directors else 'N/A'
        genres = movie.get('genres')
        genre = ', '.join(genres) if genres else 'N/A'

        print(f"Title: {title}")
        print(f"Rating: {rating}")
        print(f"Year: {year}")
        print(f"Director: {director}")
        print(f"Genre: {genre}")
    except Exception as e:
        print(f"Error during testing: {e}")


if __name__ == '__main__':
    test_imdbpy() 