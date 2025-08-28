# Hangman Game
import random
from handman_data import logo,word_list

print(logo)

choice_word = random.choice(word_list)
print(f"The chosen word is {choice_word}")

display = ["_" for _ in choice_word]
lives = 6  

while "_" in display and lives > 0:
    print("\nCurrent word:", " ".join(display))
    print(f"Lives left: {lives}")
    user_letter = input("Enter a letter: ").lower()
    if user_letter in display:
        print("you already gusee this letter")
    if user_letter in choice_word:
        for n in range(len(choice_word)):
            if choice_word[n] == user_letter:
                display[n] = user_letter
    else:
        print(f"'{user_letter}' is not in the word.")
        lives -= 1

if "_" not in display:
    print("\n🎉 Congratulations! The word is:", "".join(display))
else:
    print("\n💀 You lost the game. The word was:", choice_word)
