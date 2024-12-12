def display_results(student_names, grades, averages, letter_grades):
    """Displays the results for all students."""
    print("\n--- Student Grades and Results ---")
    for i in range(len(student_names)):
        print(f"\nStudent: {student_names[i]}")
        print(f"Grades: {grades[i]}")
        print(f"Average: {averages[i]:.2f}")
        print(f"Letter Grade: {letter_grades[i]}")
