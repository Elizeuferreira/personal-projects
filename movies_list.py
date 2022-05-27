movies = []

name = None

while name != "end":
    name = input("Type the name of a favorite movie: ")

    if name != "end":
       movies.append(name)
 
print()
print("here is your list of movies:")

for movie in movies:
    print(movie)
