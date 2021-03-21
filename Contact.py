from datetime import datetime
from uuid import uuid4

class Contact:
	def __init__(self, _name, _number):
		self.id = datetime.now().strftime("%Y%m-%d%H-%M%S-") + str(uuid4())
		self.name = _name
		self.number = _number
	
	def __repr__(self):
		return f"<Id: {self.id}, Name: {self.name}, Number: {self.number}>;"



