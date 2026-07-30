with open("sample.txt", "r") as song:
    lines = song.readlines()
    print(lines)

    for index, line in enumerate(lines):
        print(index, line)