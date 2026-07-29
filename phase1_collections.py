lucky_numbers = [42, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers.sort(reverse=True)
friends.sort()
friends2 = friends.copy()
print(friends)

coordinates = (4, 5) # Tuples cannot be modified, but lists can.
print(coordinates[1])

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
                                    # [] are used for looking up, while () are for calling a function
print(monthConversions.get("Slu", "Not a valid Key")) 
print(monthConversions.get("Jan", "Not a valid Key"))


# 1. A list of 5 favorite movies (strings). 
# Print the whole list, then print just the first and last items 
# using indexing.

favorite_movies = ["Pirates of the Carribean", "Assassins Creed", "Vinland Saga", "Doctor Who", "Spiderman"]
print(favorite_movies)
print(favorite_movies[0], favorite_movies[4])

# 2. A dictionary for a person with keys "name", "age", 
# "favorite_color". Print the whole dictionary, then print just 
# "age" by key.

myDictionary = {
    "name": "Mike",
    "age": 26,
    "favorite_color": "Purple",
}

print(myDictionary)
print(myDictionary["age"])
