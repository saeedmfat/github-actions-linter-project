# app.py
def hello_world():
    # This function has a syntax error and style issues
    print( "Hello, World!" )  # E202: whitespace after '(' and before ')'
    unused_variable = 42      # F841: local variable is assigned to but never used

def bad_indentation():
# E111: indentation is not a multiple of 4
  print("This indentation is wrong")

def long_function_name_with_many_words_and_letters(parameter_one, parameter_two): 
    # E501: line too long (90 > 79 characters)
    return parameter_one + parameter_two

# W292: no newline at end of file
