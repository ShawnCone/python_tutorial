
# Problem Set: Commenting
# Reference: https://realpython.com/python-comments-guide/

# Task 1: Uncomment a single line comment
# single_line_comment = "SOME COMMENT"

# Task 2: Uncomment a multi-line comment
# multi_line_comment = """
# SOME MULTILINE COMMENT
# """

def check():
    # Check if single_line_comment is a string
    assert isinstance(single_line_comment, str), "single_line_comment must be a string"

    # Check if multi_line_comment is a string
    assert isinstance(multi_line_comment, str), "multi_line_comment must be a string"

    print("Congratulations! You have completed problem set 0!")
    return True