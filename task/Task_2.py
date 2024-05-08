import ReadFile

data = ReadFile.process_data('data.txt')
red_duration = 0
yellow_duration = 0
green_duration = 0

for row in data:
    red_duration += row["Red"] * int(row["TimeActive"])
    yellow_duration += row["Yellow"] * int(row["TimeActive"])
    green_duration += row["Green"] * int(row["TimeActive"])

print("Red =", red_duration,"seconds", "Yellow =", "seconds",yellow_duration, "Green =", green_duration,"seconds")