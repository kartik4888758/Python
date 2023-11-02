student_info = ("Alice", 22, "Computer Science", "A")

name = student_info[0]
print(f"Student name: {name}")

num_elements = len(student_info)
print(f"Number of elements in the tuple: {num_elements}")

grade_count = student_info.count("A")
print(f"Count of 'A' grades: {grade_count}")

major_index = student_info.index("Computer Science")
print(f"Index of 'Computer Science': {major_index}")

courses = ("Math", "History", "English")
combined_info = student_info + courses
print(f"Combined tuple: {combined_info}")
