import ReadFile

data = ReadFile.process_data('data.txt')
green_active_times = []
for row in data:
    if row["Green"] > 0:
        green_active_times.append(row["Time"])

print("Times when Green was active:")
for time in green_active_times:
    print(time)