import mysql.connector
from rich import print

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
			print('Connection to the database has failed')
			raise SystemExit

# creating Db_Connection object to initialize the connection to the database
db_connection = Db_Connection('localhost','root','mysql_db1234','stock_ms');
print('[bold green][++]Connection to the database has passed')

