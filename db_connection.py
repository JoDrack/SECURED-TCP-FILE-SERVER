import mysql.connector

class Db_Connection(object):
	database_obj = None

	def __init__(self,host,user,password,database):
		self.host = host
		self.user = user
		self.password = password
		self.database  = database

		try:
			Db_Connection.database_obj = mysql.connector.connect(
			host = self.host,
			user = self.user,
			password = self.password,
			database = self.database,
		)

		except Exception as db_connection_err:
			print('Connection to the Db has failed')
			raise SystemExit

# creating Db_Connection object to initialize the connection to the database
db_connection = Db_Connection('localhost','root','@deltageronimo24','stock_ms');
