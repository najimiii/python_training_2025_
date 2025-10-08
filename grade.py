grades = {
    1.0: {"min": 97, "max": 100},
    1.25: {"min": 94, "max": 96.99},
    1.5: {"min": 91, "max": 93.99},
    1.75: {"min": 88, "max": 90.99},
    2.0: {"min": 85, "max": 87.99},
    2.25: {"min": 82, "max": 84.99},
    2.5: {"min": 79, "max": 81.99},
    2.75: {"min": 76, "max": 78.99},
    3.0: {"min": 75, "max": 75.99},
    5.0: {"min": 0, "max": 74.99}
}

def grade_conversion(score):
    for grade, range_dict in grades.items():
        if range_dict["min"] <= score <= range_dict["max"]:
            return grade

try:
    score = float(input("Enter raw grade: "))
    score = max(0, min(score, 100))
    print(f"Final grade is: {grade_conversion(score)}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
