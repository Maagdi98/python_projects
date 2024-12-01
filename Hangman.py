import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words =["bad", "good", "ugly","love","ronaldol"]
choice = random.choice(words)
# print(choice)
latters = ["_"] * len(choice)
print(" ".join(latters))
rebet = []
tries = 6
while "_" in latters and tries > 0 :
    print(HANGMANPICS[6-tries])
    
    guess = input("\nPlease guess a latter : ").lower()
    for i in range(len(choice)) : 
        if  choice[i] == guess : 
            latters[i] = guess
    if guess not in choice and guess not in rebet :
        tries -=1
        print(HANGMANPICS[6-tries])
        print(f"You have {tries} more tries")
    else: 
        print(f"You have {tries} more tries")

    if guess not in rebet : 
        rebet += guess

    else:  
        print(f"You already guessed '{guess}'. try again")  

    print(" ".join(latters))

    if "_" not in latters : 
        print("\n" + "You Win!".center(80,"*")) 

    elif tries == 0 : 
        print("\n" + "You lose!".center(80,"*"))
        print(HANGMANPICS[6-tries])
        print(f"\nThe word was '{choice}'")



def agjs():
    return print("sdad") 

