


def calculate_grade(score, pointspossible):
    '''
    Calculate the letter grade based on the score and points possible
    A - 100 - 90%
    B - 89 - 80%
    C - 79 - 70%
    D - 69 - 60%
    F - 59 - 0%
    '''
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    elif score >= 0 and score <= 59:
        return "F"
    else:
        print("Invalid score")
        exit()

# Get input (grade value from 0 to 100) from the user and store it in a variable
# Check the grade value is valid or not (0 <= grade <= 100)
# If the grade is valid, print the corresponding letter grade
# If the grade is not valid, print an error message
studentname = input("Please enter the student's name: ")

try:
    pointspossible = int(input("Please enter the total points possible: "))
    score = int(input("Please enter the score: "))
    grade = calculate_grade(score, pointspossible)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# print the student's name, score, total points possible, and letter grade
print("Student Name: " + studentname)
print("Score: " + str(score) + "/" + str(pointspossible))
print("Grade: " + grade)

