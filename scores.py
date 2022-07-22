from db import Database
from tabulate import tabulate
def displaytopscores():
	with Database() as db:
		query = "SELECT username, score FROM scores ORDER BY score DESC LIMIT 5"

		topscores = db.execute(query, fetch=True)
		print(tabulate(topscores,["#","USERNAME", "SCORE"],tablefmt="grid",showindex=range(1,6)))
def addscore(username,score):
	with Database() as db:
		query = "INSERT INTO scores(username,score) VALUES(?,?)"
		db.execute(query,(username,score))


		