from db import Database
from termcolor import cprint

pprint = lambda x: cprint(x, color="red", attrs=['bold'])

def create_user(username, password):
	with Database() as db:
		db.execute("INSERT INTO users(username, password) VALUES(?,?)",(username, password)) #creates row of user in the table

def userexists(username):
	with Database() as db:
		if(len(db.execute("SELECT username FROM users WHERE username = ?",values=(username.lower(),),fetch=True)) > 0): #This checks to see if there is already a user
			return True 	#The user exists
		else:
			return False 	#The user does not exist
def getpassword(username):
	with Database() as db:
		return db.execute("SELECT password FROM users WHERE username=?",values=(username.lower(),), fetch=True)[0][0]

def validateuser(username, password):
	if(not userexists(username)):
		pprint("***USERNAME DOES NOT EXIST***")
		return False
	actualpassword = getpassword(username)
	
	if(actualpassword == password):
		return True
	else:
		pprint("***USERNAME AND PASSWORD DO NOT MATCH***")