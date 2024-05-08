def process_data(file_path='data.txt'):
    file = open(file_path, 'r')
    lines = file.readlines()
    modified = []
    for line in lines[1:]:
        values = line.strip().split(',')
        red = int(values[0])
        yellow = int(values[1])
        green = int(values[2])
        time_active = values[3]
        time = values[4]
        row_data = {
            "Red": red,
            "Yellow": yellow,
            "Green": green,
            "TimeActive": time_active,
            "Time": time
        }
        modified.append(row_data)
    return modified


data = process_data()
#for row in data:
#    print(row)
