
# def conversion(grade:float)->float:
#     if grade < 0: return 'Invalid input'
#     elif grade <= 75: return 5.00
#     elif grade <= 75.99: return 3.00
#     elif grade <= 78.99: return 2.75
#     elif grade <= 81.99: return 2.50
#     elif grade <= 84.99: return 2.25
#     elif grade <= 87.99: return 2.00
#     elif grade <= 90.99: return 1.75
#     elif grade <= 93.99: return 1.50
#     elif grade <= 96.99: return 1.25
#     elif grade <= 100: return 1.00
#     else: return 'Invalid input'

# try:
#     raw_grade = input('Enter Raw Grade: ')
#     print(f'Final Grade: {conversion(float(raw_grade))}')
# except ValueError:
#     print("Invalid input. Please enter a number.")


# =============================================
# IKARU VERSION


# grade_dict = {
#         97: 1.0,
#         94: 1.25, 
#         91: 1.5,
#         88: 1.75, 
#         85: 2.0,
#         82: 2.25,
#         79: 2.5,
#         76: 2.75,
#         75: 3.0
#     }

# def convert_grade(grade:float)->float:
    
#     if grade > 100 or grade < 0: return "invalid grade"
    
#     for key in grade_dict:
#         if  grade >= key:
#             value =  grade_dict[key]
#             return value 
    
#     return 5.00

# grade = float(input("Enter Raw Grade: "))
# print(f"Final Grade: {convert_grade(grade)}")


# =============================================


grade_dict = {
        97: 1.0,
        94: 1.25, 
        91: 1.5,
        88: 1.75, 
        85: 2.0,
        82: 2.25,
        79: 2.5,
        76: 2.75,
        75: 3.0
    }

def convert_grade(grade:float)->float:
    
    if grade > 100 or grade < 0: return "invalid grade"
    
    for key in grade_dict:
        if  grade >= key:
            value =  grade_dict[key]
            return value 
    
    return 5.00

try:
    grade = float(input("Enter Raw Grade: "))
    print(f"Final Grade: {convert_grade(grade)}")
except ValueError:
    print("Invalid input. Please enter a number.")
