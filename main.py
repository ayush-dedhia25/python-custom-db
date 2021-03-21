from DB_Config import allRecords, insertRecord, deleteRecord, findById
from Contact import Contact

if __name__ == "__main__":
	# insertRecord(str(Contact("Test 5", "0101010101")))
	# Getting the list of all the records
	records = allRecords()
	for rec in records:
		print(rec)
	# delete = deleteRecord("202103-2113-2112-29173883-f230-4eaf-83c5-d45db2b66094")
	# find = findById("202103-2113-2045-f82dc77c-ed83-435a-943b-42d991c4d99b")