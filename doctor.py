"""
program: doctor.py
Chapter 5 Case Study (pages 138 - 139)
3/5/2026

Application that simulates a therapy session by modifying user input.
"""

import random

# Global variables of list objects that all functions can share
hedges = ("Please, tell me more...", "Many of my patients tell me the same thing.", "Please, continue.", "You don't say...", "Go on, go on...", "That's interesting...")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am":"are", "you":"I", "are":"am"}

# Definition of the reply() function
def reply(sentence):
	"""Builds and returns a reply to the sentence passed to this function."""
	probability = random.randint(1, 4)
	if probability == 1:
		return random.choice(hedges)
	else:
		return random.choice(qualifiers) + changePerson(sentence)

# Definition of the changePerson() function
def changePerson(sentence):
	"""Replace first-person words with second-person"""
	words = sentence.split()
	replyWords = []
	# FOR loop that looks at the 'words' list
	for word in words:
		replyWords.append(replacements.get(word, word))
	return " ".join(replyWords)

# Defintion of the main() function
def main():
	"""Handles the interaction between patient and doctor"""
	print("Good day, I hope you are well today.")
	print("What can I do for you?\nEnter your response or type QUIT to exit.")
	while True:
		sentence = input("\n>>")
		if sentence.upper().strip() == "QUIT":
			input("Have a great day! Press ENTER to exit.")
			break
		elif sentence == "":
			print("Did you mean to say something? Or you can type QUIT to exit.")
		else:
			print(reply(sentence))

# Global call to main() for program entry
if __name__ == '__main__':
	main()