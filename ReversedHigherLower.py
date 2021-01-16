from answerfunc import answer
def start():
	play = answer("Do you want to play?\n", ["yes", "y", "yep"], ["no", "n", "nope"])
	while True:
		if play == True:
			print("Great!\nI will think a number between 1 and 1000.\nWhat you have to do is guess if the next number will be higher or lower!")
			break
		elif play ==False:
			print("OK. See you later!")
			exit()
		else:
			print("That's not an option.")
			play
			break


def game_round():	# Higher or Lower Game starts here
	from random import randint
	known_number = randint(1, 1000)
	hidden_number = randint(1, 1000)
	print("Current Number: " + str(known_number))
	userGuess = input("Will the next number be higher (+) or lower (-)? ")
	##'higher' response
	higher = ["+", "higher", "HIGHER","higher".title(), "plus"]
	##'lower' response
	lower = ["-", "lower", "LOWER","lower".title(), "minus"]
	##both responses
	answers2 = (higher + lower)
	##this will help later
	if userGuess in higher:
		user_guessed_higher = True
	elif userGuess in lower:
		user_guessed_higher = False
	#IFs and ELIFs start here
	##if user's selection is not inside higher or lower
	if userGuess not in answers2:
		print("That's not an option.")
		return game_round()
	##CPU checks if user has lost the round, loss probabilities
	if user_guessed_higher == True and hidden_number < known_number or user_guessed_higher == False and hidden_number > known_number:
		print("Number: " + str(hidden_number))
		print("No! it was not", str(userGuess), "!", "you lost!")
        ##CPU checks if user has won the round, win probabilities
	elif user_guessed_higher == True and hidden_number > known_number or user_guessed_higher == False and hidden_number < known_number:
		print("Number: ", str(hidden_number))
		print("Congrats! You won!")

##repeat func
def repeat():
	repeat = answer("Would you like to continue playing?\n", ["y", "yes", "yep"], ["no", "n", "nope"])
	while True:
		if repeat == True:
			game_round()
			continue
		elif  repeat == False:
			print("OK. See you later!")
			exit();
		else:
			repeat


##run
start()
game_round()
repeat()
