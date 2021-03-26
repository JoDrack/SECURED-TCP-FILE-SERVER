import mysql.connector
from rich import print

class Database_Connection:
	db_conn = None

	def __init__(self,host,user,password,database):
		self.host = host
		self.user = user
		self.password = password
		self.database = database

		# calling the try_connection to get connected to the server and database if everyting is right
		self.try_connection

	@property	
	def try_connection(self):
		# trying the connection to the database
		try:
			Database_Connection.db_conn = mysql.connector.connect(
				host = self.host,
				user = self.user,
				password = self.password,
				database = self.database
				)

			# creating a cursor object to execute some SQL commands in python
			myCursor = Database_Connection.db_conn.cursor()
			print(f'[yellow][+++]Connection has been established with the database -> [blue] {self.database} [blue]')

		# catching Exceptions if any
		except Exception as db_conn_err:
			print(f'[bold red]The connection has failed[/bold red] -> [bold yellow]{db_conn_err}')
			raise SystemExit()

db_connection = Database_Connection('localhost','root','mysql_db1234','server_file_db')
