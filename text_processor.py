
transcript_lines = [
    "This is the first line of the transcript.",
    "Here is a second line, a bit longer than the first.",
    "Short one.",
]

results= {}

for index, line in enumerate(transcript_lines):
    words = line.split()
    word_count = len(words)

    if word_count >= 8:
        is_flagged = True
    else:
        is_flagged = False

    results[index + 1] = {"word_count": word_count, "flagged": is_flagged}

print(results)