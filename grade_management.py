import numpy as np
from student_manager import read_student_names, read_grades
from grade_calculator import calculate_averages, assign_letter_grades
from result_printer import display_results
def main():
    student_file = 'students.txt'
    grades_file = 'grades.txt'
    student_names = read_student_names(student_file)    
    num_students = len(student_names)
    with open(grades_file, 'r') as f:
        num_subjects = len(f.readline().split())  
    grades = read_grades(grades_file, num_students, num_subjects)
    averages = calculate_averages(grades)
    letter_grades = assign_letter_grades(averages)
    display_results(student_names, grades, averages, letter_grades)
if __name__ == '__main__':
    main()
