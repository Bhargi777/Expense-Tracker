# student_manager.py
def read_student_names(filename):
    """Reads student names from the file and returns them as a list."""
    with open(filename, 'r') as file:
        student_names = [line.strip() for line in file.readlines()]
    return student_names
def read_grades(filename, num_students, num_subjects):
    """Reads grades from the file and returns them as a numpy array."""
    import numpy as np
    grades = np.zeros((num_students, num_subjects))
    with open(filename, 'r') as file:
        for i, line in enumerate(file.readlines()):
            grades[i] = np.array([float(x) for x in line.split()])
    return grades
