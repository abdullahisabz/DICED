from utils import yesnoinput, welcome, endgame, plural
import player
import scores
import termcolor
from tabulate import tabulate

players=[]



points = lambda x: f'point{plural(x)}'
unameprint = lambda x: termcolor.colored(x.upper(), color="blue", attrs=["bold", "blink"])

welcome()
if yesnoinput("Do you want to login and play"):
	players=player.login()

elif yesnoinput("Do you want to register a player"):
	player.register()

	while yesnoinput("Do you want to register another user"):
		player.register()

	if yesnoinput("Are you ready to login now"):
		players = player.login()
	else:
		endgame()
else:
	endgame()

def round(roundnumber):

	roundprint= lambda x: termcolor.cprint(("\n"+("*"*5) + " " + x + " " + ("*"*5)+"\n"),'blue', attrs=['bold'])
	roundprint("WELCOME TO ROUND " + str(roundnumber))
	players[0].newround()
	players[1].newround()
	for n in range(2):
		input(f"\n{unameprint(players[n].username)} Press Enter to roll your first dice ...")
		dice1 = players[n].rolldice()
		input("\nPress Enter to roll your second dice ...")
		dice2 = players[n].rolldice()
			


		if (dice1 + dice2) % 2 == 0:
			players[n].updatescore(10)
			print(unameprint(players[n].username) + " you get 10 points added to your score\n")
		else:
			players[n].updatescore(-5)
			print(unameprint(players[n].username) + " you get 5 points deducted from your score\n")
		if dice1==dice2:
			input(f"{unameprint(players[n].username)} You get to roll another dice\nSo Press Enter to roll")
			players[n].rolldice()


	roundtable= [["USERNAME","POINTS AT END OF ROUND", "TOTAL POINTS"]]
	for n in range(2):
		roundtable.append([players[n].username.upper(), players[n].roundscore, players[n].score])
	print("\n"+tabulate(roundtable,headers="firstrow",tablefmt="grid"))

	roundprint(f"ROUND {roundnumber} HAS ENDED")

if len(players) != 0:
	for roundn in range(1,6):
		round(roundn)

	while players[0].score == players[1].score:
		input(f"{players[0].username} Press Enter to roll your a dice ...")
		dice1 = players[0].rolldice()
		input(f"{players[1].username} Press Enter to roll your a dice ...")
		dice2 = players[1].rolldice()
	
	scores.addscore(players[0].username, players[0].score)
	scores.addscore(players[1].username, players[1].score)
	scores.displaytopscores()

	def winprint(x=1): 
		if x==1:
			return termcolor.colored("YOU ARE THE WINNER", color='cyan', attrs=['bold'])
		else:
			return termcolor.colored("CONGRATS", color='cyan', attrs=['bold'])

	if players[0].score > players[1].score:
		print(f"\n{winprint(0)} {unameprint(players[0].username)} {winprint()}\n")
	else:
		print(f"\n{winprint(0)} {unameprint(players[1].username)} {winprint()}\n")
	endgame()