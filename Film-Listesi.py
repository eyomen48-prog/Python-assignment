movies = [
{"title": "Film A", "rating": 7.2},
{"title": "Film B", "rating": 8.9},
{"title": "Film C", "rating": 8.1},
{"title": "Film D", "rating": 9.0},

]
print(sorted(movies, key=lambda x: x["rating"], reverse=True)[:3])
for film in sorted(movies, key=lambda x: x["rating"], reverse=True)[:3]:
    print(film["title"])