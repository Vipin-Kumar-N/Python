currentMovies = {
    "2012" : "11:30 AM",
    "Home" : "2:00PM",
    "2018" : "6:30PM"
}

for movie in currentMovies:
    print(movie)
search = input("Enter the Movie Name : ")
showtime = currentMovies.get(search)
if showtime:
    print(search,"Playing on : ",showtime)
else:
    print("No Show Time Available for the movie !!!")