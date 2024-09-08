text = "  Hello, world!  "
new_text = text.replace(" ", "")
print(new_text)  # Output: "Helloworld!"
## Problem 1 ##
#Fix the following code so that its output matches
# Sample output:
# --------------------------------------------------
# my name is Tim Tester, I am 20 years old
# 
# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)
#  
# I am looking for a job with a salary of 2000-3000 dollars per month

name = "Tim Tester"
age = 20
skills = [
    ("python", "beginner"),
    ("java", "veteran"),
    ("programming", "semiprofessional"),
]
salary_range = (2000, 3000)

print("my name is", name, ", I am", age, "years old\n")
print("my skills are")
for skill, level in skills:
    print(" -", skill, "(",  level, ")")
print("\n")
print("I am looking for a job with a salary of", salary_range[0], "-", salary_range[1], "dollars per month")


## Problem 2 ##
#Please finish the script so that: 
# - the following output is printed:
# Sample output:
# --------------------------------------------------
# X val: 27
# Y val: 15
#
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8
#
# - The program should work correctly even if the values of the variables are changed.

x = input("X val: ")
y = input("Y val: ")

print(int(x) + int(y))
print(int(x) - int(y))
print(int(x) * int(y))
print(int(x) / int(y))
