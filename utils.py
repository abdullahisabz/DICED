import termcolor
import user



def getinput(prompt=""):	# Gets input from the user but also
							# that they did not leave the field
							#empty.
	getin = input(prompt)
	while(len(getin) == 0):
		print("You cannot leave this field empty")
		getin = getinput(prompt)
	return getin

def yesnoinput(prompt):	# Handles inputs that involves yes or 
						# no questions.

	# Dictionary to map inputs to whether they are true or
	# false.
	yesno = {
		'N': False,
		'Y': True
	}

	# Adds additional infomation for the user when
	# using yes or no input to identify the form of input
	# they need to give.

	cin = getinput(prompt + " Yes[Y] No[N]: ").upper()[0]	

	while cin not in ['Y','N']:			# Checking to see whether answer
										# is a yes or not answer
		
		print("You must enter 'Y' or 'No'" + '')
		cin = yesnoinput(prompt)

	return yesno[cin]


titleprint1 = lambda x: termcolor.cprint(x, 'cyan', attrs=['bold'])
titleprint2 = lambda x: termcolor.cprint(x, 'white', attrs=['bold'])
def welcome():
	titleprint1("|----------------------------------------------------|")
	titleprint1("|----------------------------------------------------|")
	titleprint1("|----------------                    ----------------|")
	titleprint2("                   WELCOME TO DICED                   ")
	titleprint1("|----------------                    ----------------|")
	titleprint1("|----------------------------------------------------|")
	titleprint1("|----------------------------------------------------|")

def endgame():
	titleprint1("|----------------------------------------------------------|")
	titleprint1("|----------------------------------------------------------|")
	titleprint1("|-----------------                         ----------------|")
	titleprint2("                    THANK YOU FOR PLAYING                   ")
	titleprint1("|-----------------                         ----------------|")
	titleprint1("|----------------------------------------------------------|")
	titleprint1("|----------------------------------------------------------|")

def plural (x): 
	if x != 1: 
		return 's'
	