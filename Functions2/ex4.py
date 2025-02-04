def ex4(movies):
    return sum(m["imdb"] for m in movies) / len(movies) if movies else 0
