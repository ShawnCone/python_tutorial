# Problem Set: If/Else/Elif Statements

# Reference: https://realpython.com/python-conditional-statements/

# Replace ?? with the correct answer(s)
condition_1 = ?? 
condition_2 = ?? 

condition_3 = ?? 
condition_4 = ?? 


### DO NOT CHANGE THE CODE BELOW ###

CORRECT_ANS_VALUE = 100

if condition_1:
    ans_1 = CORRECT_ANS_VALUE # Make condition_1 a boolean that allows ans_1 to have value 10

# Task 2: Write an if/else statement
if condition_2:
    ans_2 = 0
else:
    ans_2 = CORRECT_ANS_VALUE

# Task 3: Write an if/elif/else statement
if condition_3:
    ans_3 = 0
elif condition_4:
    ans_3 = CORRECT_ANS_VALUE
else:
    ans_3 = 0
### DO NOT CHANGE THE CODE ABOVE ###



def check():
    # Check if task1_condition is a boolean
    assert isinstance(ans_1, CORRECT_ANS_VALUE), "condition_1 is incorrect"

    # Check if task2_condition is a boolean
    assert isinstance(ans_2, CORRECT_ANS_VALUE), "condition_2 is incorrect"

    # Check if task3_condition is a boolean
    assert isinstance(ans_3, CORRECT_ANS_VALUE), "condition_3 is incorrect"

    return True