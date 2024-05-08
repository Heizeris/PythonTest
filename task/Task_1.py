import ReadFile

data = ReadFile.process_data('data.txt')

red_count= 0
yellow_count = 0
green_count = 0
for row in data:
    red_count += row["Red"]
    yellow_count += row["Yellow"]
    green_count += row["Green"]


print("red =", red_count, "yellow =", yellow_count, "green =", green_count)