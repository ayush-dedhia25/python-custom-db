import os
from utilities import convertToStr

# Defining the db file :)
DB_FILE = "db.dms"

# Logic for adding a record to the database
def insertRecord(_object):
	try:
		# Checking if the file is not empty
		if os.stat(DB_FILE).st_size != 0:
			with open(DB_FILE) as db:
				content = db.read()
				with open(DB_FILE, "w") as db:
					content += "\n" + _object
					db.write(content)
					db.close()
					print("Record added!")
				db.close()
		# If the file was empty then do not add the newline before the first record
		else:
			with open(DB_FILE) as db:
				# Reading the contents of the db file as a text format
				content = db.read()
				with open(DB_FILE, "w") as db:
					# A hack to append the new record to the db file
					content += _object
					db.write(content)
					db.close()
					print("Record added!")
				db.close()	
	except FileNotFoundError:
		raise Exception("Database is missing! Please fix it!")

# Logic for deleting a record from the database
def deleteRecord(_id):
	records = []
	
	try:
		with open(DB_FILE) as dbFile:
			# Step 1 => Fetch all the records
			rawRecords = dbFile.readlines()
			# Step 2 => Remove all the unwanted characters from each record
			for x in rawRecords:
				x = x.replace("<", "")
				x = x.replace(">", "")
				x = x.replace(";", "")
			# Step 3 => Remove newline character
				x = x.replace("\n", "")
			# Step 4 => Extract all the fields from the record
				x = x.split(", ")
			# Step 5 => Add all the records to the list
				records.append(x)
				
			for eachRecord in records:
				id_ = eachRecord[0].split("Id: ")[1]
				# name = eachRecord[1].split("Name: ")[1]
				# number = eachRecord[2].split("Number: ")[1]
				
				# Compare the record_id with provided_id
				if _id == id_:
					records.remove(eachRecord)
					break
			
			for current in range(len(records)):
				# Converting a list to string
				records[current] = convertToStr(records[current], ", ")
				# Add a special characters at the leading and trailing of the string
				# Preventing to add a new line character after the last record
				if current == len(records) -1:
					records[current] = "<" + records[current] + ">;"
				else:
					records[current] = "<" + records[current] + ">;\n"
		
			with open(DB_FILE, "w") as dbFile:
				# Updating the db file
				dbFile.writelines(records)
				dbFile.close()
				print("Record deleted!")
				
	except FileNotFoundError:
		raise Exception("File not found error!")

# Logic for searching a record by its `ID` from the database
def findById():
	pass

# Logic for fetching all the records from the database
def allRecords():
	# Characters to be excluded from the string
	bad_character = '<>"";'
	all_records = []
	refined_set = []
	
	try:
		with open(DB_FILE, "r") as db:
			records = db.readlines()
			for i in records:
				for char in bad_character:
					# Stripping off all the unwanted characters
					i = i.replace(char, "")
				# Removing the line breaks from the string
				i = i.replace("\n", "")
				# Adding the final sanitized string to the records list
				all_records.append(i)
	# Throws an FileNotFound exception if the db file is not found			
	except FileNotFoundError:
		print("database is not found!")

	for record in all_records:
		# Extracting each field from the plain record string
		record = record.split(",")
		# Constructing an object of each record
		_ = {
			"ID": str(record[0].strip().split("Id: ")[1]),
			"Name": record[1].strip().split("Name: ")[1],
			"Number": record[2].strip().split("Number: ")[1]
		}
		# Pushing the record object into the refined_set list
		refined_set.append(_)
	# Return the list of all records object
	return refined_set