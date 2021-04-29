# This is the main Python file that runs the game
import random
def getWords():
  # This function gets the playable words
  with open("english-words.txt","r") as file:
    contents = file.readlines()
    words = []
    for word in contents:
      words.append(word.strip())
    return words

def getLetterGuess(used):
  # This function gets the single character guess from the plr
  guess = input("Please type ONE character to guess: ")
  if len(guess) != 1 :
    print("Invalid input. Please enter only ONE character")
    return getLetterGuess(used)
  elif guess in used:
    print("Invalid input. You have already guessed {} already.".format(guess))
    return getLetterGuess(used)
  
  return guess

def fillInLetters(word,blanks,character):
  # This function fills in the words based on the input
  pair = zip(word,blanks)
  new_word = ""
  

  for wc,bc in pair:
    if bc == "_" and wc == character:
      new_word += character
    else:
      new_word += bc
  return new_word

def exists(character,word):
  # checks if the character exists in the word
  return character in word

def gameRound():
  # Plays one whole round of Hangman until failure or success
  words = getWords()

  chosenword = words[random.randrange(0,len(words)-1)]
  current_filled = "_"*len(chosenword)
  current_lives = 6
  used = ""

  while current_filled != chosenword and current_lives>0:
    temp = "".join([l + " " for l in current_filled])
    print("So far you have: {}".format(temp))
    print("You have {} lives so far and have guessed these letters so far: {} \n".format(current_lives,used))


    userinput = getLetterGuess(used)
    used += userinput
    isInWord = exists(userinput,chosenword)

    if isInWord:
      wrd = fillInLetters(chosenword,current_filled,userinput)
      print("Correct! '{}'' is a letter in the word.".format(userinput))
      current_filled = wrd
    else:
      current_lives -=1
      print("Incorrect! -1 life.")
  if current_filled == chosenword:
    print("\nYou win! The correct word was {} and you got it! \n".format(chosenword))
  elif current_filled != chosenword or current_lives <=0:
    print("\nYou lost... The correct word was {}.\n".format(chosenword))

  replay = input("Would you like to play again? 'YES' to replay, type anything else to quit the game: ")
  if replay.lower() == "yes":
    print("\n \n")
    gameRound()


print("Welcome to Hangman! You will have 6 attempts to guess each word. If you guess the word, you win! The first round will be starting now. \n")

gameRound()
