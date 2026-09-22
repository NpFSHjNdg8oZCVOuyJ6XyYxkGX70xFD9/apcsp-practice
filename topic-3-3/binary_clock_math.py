clock_values = [13, 42]
labels = ["Hours","Minutes"]
clock_values.append(17)
labels.append("Seconds")
selected_index = 2 # using the same index keeps the value and label together so its easier to add more
clock_value = clock_values[selected_index]
label = labels[selected_index]

remaining = clock_value
bits = []

bits.append(remaining % 2)
remaining = remaining // 2

bits.append(remaining % 2)
remaining = remaining // 2

bits.append(remaining % 2)
remaining = remaining // 2

bits.append(remaining % 2)
remaining = remaining // 2

bits.append(remaining % 2)
remaining = remaining // 2

bits.append(remaining % 2)

bits.reverse()

bit_text = str(bits[0]) + str(bits[1]) + str(bits[2]) + str(bits[3]) + str(bits[4]) + str(bits[5])
check_value = bits[0] * 32 + bits[1] * 16 + bits[2] * 8 + bits[3] * 4 + bits[4] * 2 + bits[5] * 1
print("Selected index: " + str(selected_index))
print(str(label) + ": " + str(clock_value) + " --> " + str(bit_text))
print("Original: ", str(clock_value) + ", " + "Reconstructed: " + str(check_value))