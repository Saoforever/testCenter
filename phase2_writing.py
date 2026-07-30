with open("output.txt", "w") as f:
    f.write("Got something in my system\n")
    f.write("She said, \"Why you gotta take it so far?\"\n")
    f.write("Excuse me, I'm out of rhythm\n")

with open("output.txt", "r") as f:
    print(f.read())