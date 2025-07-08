# function with output
# which means a function that make return it's output based on 'return' keyword
# e.g. return my fulll name in sentence format
def sentence_format(first_name,last_name):
    formated_f_name=first_name.title()
    formated_l_name=last_name.title()
    return f"{formated_f_name} {formated_l_name}" 

first_name=input("Enter your first name?:")
last_name=input("Enter your last name?:")
print(sentence_format(first_name=first_name,last_name=last_name))
