import pandas as pd

# Load Excel data
data = pd.read_excel("student_data.xlsx")

# Calculate average marks
average_marks = data["MARKS"].mean()

# Find students with attendance below 75%
low_attendance = data[data["ATTENDANCE"] < 75]

print("Average Marks:", average_marks)
print("\nStudents with Attendance below 75%:")
print(low_attendance)
