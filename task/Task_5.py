import ReadFile

data = ReadFile.process_data('data.txt')


mistake_count = 0

mistakes = []

for row in data:

    if sum([row["Red"], row["Yellow"], row["Green"]]) != 1:

        mistake_count += 1
        if row["Red"] + row["Yellow"] + row["Green"] == 0:
            mistake_type = "No colors active"
        else:
            mistake_type = "Multiple colors active"
        mistakes.append({"Time": row["Time"], "Mistake": mistake_type})


print("Number of lines with mistakes:", mistake_count)
for mistake in mistakes:
    print("Time:", mistake["Time"], "- Mistake:", mistake["Mistake"])