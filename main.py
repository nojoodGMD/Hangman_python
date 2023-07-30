#Hello! Welcome to my first project using Python
#Have fun :D

import random
import hangman_words
import hangman_art

# 1.print logo
print(hangman_art.logo)

# 2.choose a random word
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# 3.Print the '_'
dashes = []
for _ in range(word_length):
  dashes.append("_")

# 4.let the user guess
print("Hint! The word is "+chosen_word)

# 5.check if the guess is correct
lives = 6
end_of_game = False

while not end_of_game:
  guess = input("Enter yout guess: ").lower()

  # 6.1 Check if the user already guesed the letter
  if guess in dashes:
    print(f"Yoy have already guessed {guess} before, try another letter.")
    continue

  # 6.2 Check if the letter does not exits the the chosen_word
  if guess not in chosen_word:
    lives-=1
    print(f"Wrong answer, the letter {guess} does not exist in the chosen word.\n")

    if lives == 0:
      print("You lose :(")
      print(hangman_art.stages[lives])
      end_of_game =True
      continue

  #6.3 if all above was not exeuted, then the guess is correct, replace each '_' with the correct letter
  # if the user already guessed the letter, send a messege and repeat the cycle

  if guess in dashes:
    print(f"You have already guessed the letter {guess}")
    continue

  #replace all the '_' with the correct letter
  for index in range(word_length):
    if chosen_word[index] == guess:
      dashes[index] = guess


  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(dashes)}")
  
  # 6.4 if all the dashes disappeared, the user wins
  if '_' not in dashes:
    print("You win!")
    end_of_game = True

  #print the stage
  print(hangman_art.stages[lives])
    

