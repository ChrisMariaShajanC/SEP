movies = []
for i in range(3):
    movie = input("Enter favorite movie:")
    movies.append(movie)
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(movie.upper() + "\n")
        

print("\nMovies in uppercase:")
with open("movies.txt", "r") as file:
    for line in file:
        print(line.strip().upper())