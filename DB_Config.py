import os
from utilities import convertToStr, removeCharacters, extractFields, constructObject

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
	filter_out_record = None
	
	try:
		with open(DB_FILE) as dbFile:
			# Step 1 => Fetch all the records
			rawRecords = dbFile.readlines()
			# Step 2 => Remove all the unwanted characters from each record
			rawRecords = removeCharacters(rawRecords)
			
			for current_rec in rawRecords:
				records.append(current_rec)

			for eachRecord in records:
				# Extracting each field from the record
				rec_id, rec_name, rec_num = extractFields(eachRecord)
   			# Compare the record_id with provided_id
				# If _id matches with the record's id then delete that record
				# And update the db file
				if _id == rec_id:
					filter_out_record = eachRecord
					records.remove(eachRecord)
					
					for current in range(len(records)):
						# Converting a list to string
						records[current] = convertToStr(records[current], ", ")
						# Preventing to add a new line character after the last record
						if current == len(records) -1:
							# Adding a special characters at the leading and trailing of the string
							records[current] = "<" + records[current] + ">;"
						else:
							records[current] = "<" + records[current] + ">;\n"

					with open(DB_FILE, "w") as dbFile:
						# Updating the db file
						dbFile.writelines(records)
						dbFile.close()
						print("Record deleted!")
					# Stop the loop as we have found the desired id
					break
				
	except FileNotFoundError:
		raise Exception("File not found error!")
	
	if filter_out_record is not None:
		filter_out_record = convertToStr(filter_out_record, ", ")
		return "<" + filter_out_record + ">"
	else:
		return "No record was found with that `Id`"

# Logic for searching a record by its `ID` from the database
def findById(_id):
	searched_record = None

	try:
		with open(DB_FILE) as dbFile:
			records = dbFile.readlines()
			# Constructing the readable object
			array = removeCharacters(records)
			
			for curr in array:
				# Extracting each field from a record
				rec_id, rec_name, rec_num = extractFields(curr)
				# Filtering out the required record
				if _id == rec_id:
					searched_record = curr
					break

	except FileNotFoundError:
		raise Exception("Db file not found!")
		
	if searched_record is not None:
		searched_record = convertToStr(searched_record, ", ")
		searched_record = "<" + searched_record + ">"
		return searched_record
	else:
		return "No records found with that `Id`"
	
def fetchRecords():
	try:
		with open(DB_FILE) as dbFile:
			records = dbFile.readlines()
			records = removeCharacters(records)
			records = constructObject(records)
			return records
	except FileNotFoundError:
		raise Exception("DB file is missing!")