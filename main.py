import sqlite3

class PQL( object ):
	def __init__(self):
		self.connection = sqlite3.connect("my_db")
		self.cursor = self.connection.cursor()
		self.execute("create table if not exists user_list (username varchar(50), password md5, primary key(username))")

	def execute( self, query ):
		return self.cursor.execute(query)

	def insert(self, data):
		if self.check(data[0]) == True:
			self.execute("insert into user_list (`username`,`password`) values('" + data[0] +"', '"+data[1]+"')")
		else:
			self.error("Username exists")
	@staticmethod
	def error(msg):
		print(msg)
	def check(self, username):
		count = len(self.execute("select * from user_list where username='"+username+"'").fetchall())
		if count > 0:
			return False
		else:
			return True

	def showall(self):
		return self.execute("select * from user_list").fetchall()

	def delete(self, username):
		return self.execute("delete from user_list where username='"+username+"'")

def banner():
	var = """
	table\t\t : user_list
	show\t\t : Show current data from user_list
	insert\t\t : Insert new data into user_list
	update\t\t : Update data from user_list
	delete\t\t : Delete data from user_list
	"""
	print(var)

def preload():
	pql = PQL()
	banner()
	stat = True
	while stat:
		cmd = str(input("command_> "))
		if cmd.lower() == "insert":
			pql.insert(Insert())
		elif cmd.lower() == "show":
			print(pql.showall())
		elif cmd.lower() == "delete":
			if pql.delete(Delete()):
				print("[ * ] Success")
			else:
				print("[ ! ] Couldn't delete data")

def Delete():
	stat = True
	username = ""

	while stat:
		username += input("Username_> ")
		if username != "":
			return username
		else:
			print("[ ! ] Please username want to delete from database")
			continue
	if username != "":
		return username
	else:
		return None

def Insert():
	stat = True
	username = ""
	password = ""
	while stat:
		username += input("Username_> ")
		password += input("Password_> ")
		if username != "":
			if password != "":
				stat=False
			else:
				continue
		else:
			continue

	if username != "":
		if password != "":
			return username, password
		else:
			return None, None
	else:
		return None, None

if __name__ == "__main__":
	try:
		preload()
	except Exception as e:
		print("[ ! ] An exception has occured : "+str(e))