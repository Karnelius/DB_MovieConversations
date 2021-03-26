from data.Repo.movie_repo import store_movies


def main():
    with open('./raw_data/movie_titles_metadata.txt') as movie_data:
        lines = []
        genres = set()
        for line in movie_data:
            line = line.strip()
            line_data = line.split(' +++$+++ ')
            line_dict = {
                'movie_id': line_data[0],
                'movie_title': line_data[1].title(),
                'movie_year': int(line_data[2]),
                'IMDB_rating': float(line_data[3]),
                'IMDB_votes': int(line_data[4]),
                'genres': line_data[5][1:-2].replace("'", "").split(', ')
            }
            for genre in line_dict['genres']:
                genres.add(genre)
            lines.append(line_dict)

    store_movies(lines)
#DELETE FROM movies where movie_id != 'q99';

if __name__ == '__main__':
    main()
