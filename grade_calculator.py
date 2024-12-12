# grade_calculator.py
import numpy as np

def calculate_averages(grades):
    """Calculates the average grade for each student."""
    return np.mean(grades, axis=1)

def assign_letter_grades(averages):
    """Assigns letter grades based on the average score."""
    letter_grades = []
    for avg in averages:
        if avg >= 9:
            letter_grades.append('A')
        elif avg >= 8:
            letter_grades.append('B')
        elif avg >= 7:
            letter_grades.append('C')
        elif avg >= 6:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    return letter_grades
