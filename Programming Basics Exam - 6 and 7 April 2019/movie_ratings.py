number_movies = int(input())

top_movie = ''
top_rating = 0

lowest_movie = ''
lowest_rating = 0

ratings_sum = 0

for i in range(number_movies):
    name_movie = input()
    rating_movie = float(input())
    ratings_sum += rating_movie

    if i == 0:
        lowest_movie = name_movie
        lowest_rating = rating_movie
    if rating_movie > top_rating:
        top_movie = name_movie
        top_rating = rating_movie
    elif rating_movie < lowest_rating:
        lowest_movie = name_movie
        lowest_rating = rating_movie

average_rating = ratings_sum / number_movies

print(f"{top_movie} is with highest rating: {top_rating:.1f}")
print(f"{lowest_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")