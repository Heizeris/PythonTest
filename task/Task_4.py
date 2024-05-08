import ReadFile

data = ReadFile.process_data('data.txt')

complete_cycles = 0
sequence = ["Red", "Yellow", "Green", "Yellow", "Red"]
current_sequence_index = 0

for row in data:

    if row[sequence[current_sequence_index]] > 0:
        current_sequence_index += 1
    else:
        current_sequence_index = 0


    if current_sequence_index == len(sequence):
        complete_cycles += 1
        current_sequence_index = 0

print("Number of complete cycles Red-Yellow-Green-Yellow-Red:", complete_cycles)