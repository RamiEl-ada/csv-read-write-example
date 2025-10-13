# Reading CSV files - Student Scores Tracker
with open('1_students.csv', 'r', encoding='utf-8') as file:
    line_number = 0 
    highest_average = 0
    lowest_average = 100
    for line in file:
        row = line.strip().split(',')
        if line_number == 0:
            print(f"Headers: {row}")  # First line is the header
        else:
            name = row[0]
            scores = [int(score) for score in row[1:]]
            average = sum(scores) / len(scores)
            if average < lowest_average:
                lowest_average = average
                lowest_holder_name = name
            elif highest_average < average:
                highest_average = average
                highest_holder_name = name
            print(f"{name} - Scores: {scores} | Average: {average:.2f}")
        line_number+=1 

print(f"Highest Average: {highest_average:.2f}, Lowest Average: {lowest_average:.2f},")
print(f"Highest Average Holder: {highest_holder_name}\nLowest Average Holder: {lowest_holder_name}")

# Extension task: Modify the program to print the highest and lowest average scores among all students 
# along with the names of the students who acheived these scores.
# Try on your own and scroll down to see one possible way to solve this































# filename = '1_students.csv'

# student_averages = {}  # Store student name -> average mapping

# with open(filename, 'r', encoding='utf-8') as file:
#     line_number = 0
#     for line in file:
#         row = line.strip().split(',')
#         if line_number == 0:
#             print(f"Headers: {row}")  # First line is the header
#         else:
#             name = row[0]
#             scores = [int(score) for score in row[1:]]
#             average = sum(scores) / len(scores)
#             student_averages[name] = average
#             print(f"{name} - Scores: {scores} | Average: {average:.2f}")
#         line_number += 1

# # --- Extension Task: Find Highest and Lowest Averages ---
# print("\nSummary:")
# highest_avg = max(student_averages.values())
# lowest_avg = min(student_averages.values())

# # Find the names of students who achieved them
# top_student = [name for name, avg in student_averages.items() if avg == highest_avg][0]
# bottom_student = [name for name, avg in student_averages.items() if avg == lowest_avg][0]

# print(f"Highest average: {top_student} ({highest_avg:.2f})")
# print(f"Lowest average: {bottom_student} ({lowest_avg:.2f})")
