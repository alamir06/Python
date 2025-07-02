# hangman game
import random
word_list=["alamirew","aklilu","fqadie","temesgen"]

choice_word=random.choice(word_list)
user_letter=input("Enter a Letter:")
for n in range(len(choice_word)):
    if user_letter==choice_word[n]:
        print("Right")
    else:
        print("Wrong")