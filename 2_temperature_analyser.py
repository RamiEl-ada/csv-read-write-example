# Fill in the missing parts:
# Create a loop to go through each line in the file (2_temperatures.csv).
# Split the line by commas to separate date and temperature.
# Convert the temperature value (second part) to a float.
# Then run the program and check that:
# It correctly ignores invalid values.
# It displays the valid temperatures and statistics (average, highest, lowest).
# Try on your own and scroll down to see one possible solution

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            line.strip().split(',')
            # Skip header or malformed lines
            if len(parts) != 2 or parts[0] == "Date":
                continue
            try:
                # TODO: Convert the second part to a float
                
                numbers.append(number)
            except ValueError:
                continue  # Skip non-numeric values
            line += 1
    return numbers


# Main program
temperatures = read_numbers_from_file('2_temperatures.csv')

if temperatures:
    print(f"Valid temperatures: {temperatures}")
    print(f"Average temperature: {sum(temperatures)/len(temperatures):.2f}°C")
    print(f"Highest temperature: {max(temperatures)}°C")
    print(f"Lowest temperature: {min(temperatures)}°C")
else:
    print("No valid temperature data found.")

# Scroll down below to see the solution






































# def read_numbers_from_file(filename):
#     numbers = []
#     with open(filename, 'r') as file:
#         for line in file:
#             # Split each line by comma
#             parts = line.strip().split(',')
#             # Skip header or malformed lines
#             if len(parts) != 2 or parts[0] == "Date":
#                 continue
#             try:
#                 number = float(parts[1])
#                 numbers.append(number)
#             except ValueError:
#                 continue  # Skip non-numeric values
#     return numbers


# # Main program
# temperatures = read_numbers_from_file('2_temperatures.csv')

# if temperatures:
#     print(f"Valid temperatures: {temperatures}")
#     print(f"Average temperature: {sum(temperatures)/len(temperatures):.2f}°C")
#     print(f"Highest temperature: {max(temperatures)}°C")
#     print(f"Lowest temperature: {min(temperatures)}°C")
# else:
#     print("No valid temperature data found.")
