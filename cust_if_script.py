
#!/usr/bin/env python3


message = 'Your letter grade on this assignment is: '

grade = float(input("What is the % grade on this assignment? "))

if grade > 90 and grade <= 100:
    message = message + 'A'
elif grade <= 89 and grade > 80:
    message = message + 'B'
elif grade <= 79 and grade >= 70:
    message = message + 'C'
elif grade <= 69 and grade >= 60:
    message = message + 'D'
elif grade < 60:
    message = message + 'F'

print(message)
