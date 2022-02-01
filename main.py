

import random
import texts


end_of_game = False


from  hangman import logo
print(logo)
chosen_word = random.choice(texts.word_list2)
word_length = len(chosen_word)



print(f' the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"


lives=6
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"you alreasy gussed {guess}")

    # if guess == display:
    #     print("you have already entered this")

    for position in range(word_length):
        l = chosen_word[position]

        if l == guess:
            display[position] = l



    if guess not in chosen_word:
        lives-=1
        print("letter does not exist here")
        if lives == 0:
            end_of_game = True
            print("game over")
    print(f"{' '.join(display)}")



    if "_" not in display:
        end_of_game = True
        print("You win.")
    from  hangman import stages


    print(stages[lives])


