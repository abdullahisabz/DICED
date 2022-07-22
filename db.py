import sqlite3 as sqlite

class Database(object):
	DATABASE_LOCATION = "diced_database.db" # Database File Location

	def __init__(self):
	# Initialize db class variables
		self.connection = sqlite.connect(Database.DATABASE_LOCATION)
		self.cursor = self.connection.cursor()

		
	def __enter__(self): 
		return self

	def execute(self, query, values=(), fetch=False):
		# Fetch parameter specifies whether or rows need to be fetched e.g a SELECT statement
		if fetch == True:
			return self.cursor.execute(query, values).fetchall()	
			# If executing a SELECT statement we want to fetch all roles needed	
		else: 
			return self.cursor.execute(query, values)
			# Else we just execute the query

	def __exit__(self, ext_type, exc_value, traceback):
		self.cursor.close()
		if isinstance(exc_value, Exception):
			self.connection.rollback()
		else:
			self.connection.commit()
			self.connection.close()

