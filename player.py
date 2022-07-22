from utils import getinput
import dice
import user
from user import pprint
from termcolor import colored

class Player:
	def __init__(self, username):
		self.username = username # setting players name
		self.score = 0	# setting player score as 0
		self.roundscore = 0

	def updatescore(self,x):
		self.score+=x
		self.roundscore+=x
		if self.score < 0: self.score = 0
		if self.roundscore < 0: self.roundscore = 0

	def newround(self):
		self.roundscore=0

	def rolldice(self):
		dicen = dice.roll()
		self.updatescore(dicen)
		print("\nYou rolled a",str(dicen))
		return dicen
	
def register():
	username = getinput("What is your username: ")
	if user.userexists(username):
		pprint("***USERNAME ALREADY EXISTS***")
		register()
	if not username.isalpha():
		pprint("***YOUR USERNAME CAN ONLY BE ALPHANUMERIC***")
		register()
	if ' ' in username:
		pprint("***YOU CANNOT HAVE WHITESPACE IN YOUR USERNAME***")
		register()
	if len(username) > 35:
		pprint("***USERNAME MUST NOT BE LESS THAN 35 CHARACTERS***")
		register()
	
		
	password = getinput("What is your password: ")

	if len(password) <= 0:
		pprint("***YOUR PASSWORD CANNOT BE EMPTY***")
		register()

	user.create_user(username, password) # creating user

def login():
	players = []
	i=1
	while i <= 2:
		print(f"Sign in Player {i}")
		username = getinput("What is your username: ").lower()
		password = getinput("What is your password: ").lower()

		if user.validateuser(username, password):
			players.append(Player(username))
			i+=1

	print(colored("Thank you for logging in",color="green",attrs=['bold']))
	return players



	