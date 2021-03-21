# Function for converting a list to a key-value,
# Comma separated string
def convertToStr(array, separator):
	final_str = separator.join(array)
	return final_str
	
# Function for removing all the unwanted characters
# From every db record
def removeCharacters(array):
	for currentItr in range(len(array)):
		# Removing unwanted characters one by one
		array[currentItr] = array[currentItr].replace("<", "")
		array[currentItr] = array[currentItr].replace(">", "")
		array[currentItr] = array[currentItr].replace(";", "")
		array[currentItr] = array[currentItr].replace("\n", "")
		array[currentItr] = array[currentItr].split(", ")
		
	# Returning the manipulated array with removed unwanted characters
	return array

# Function for extracting each field from the record
# INPUT => ['ID: XXXXXXXXXX', 'Name: Test 1', 'Number: 0101010101']
def extractFields(record):
	record_id = record[0].split("Id: ")[1]
	record_name = record[1].split("Name: ")[1]
	record_number = record[2].split("Number: ")[1]
	
	return record_id, record_name, record_number
	
# Convert ['ID: XXXXXXXXXX, Name: Test 1, Number: 0101010101']
# To <ID: XXXXXXXXXX, Name: Test 1, Number: 0101010101>;
def constructDBObject(record):
	a, b, c = extractFields(record)
	return f"<Id: {a}, Name: {b}, Number: {c}>"