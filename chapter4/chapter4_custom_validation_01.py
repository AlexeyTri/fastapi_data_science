from datetime import date
from pydantic import BaseModel, ValidationError, field_validator

class Person(BaseModel):
	first_name: str
	last_name: str
	birthday: date
	@field_validator("birthday")
	def valid_date(cls, v: date):
		delta = date.today() - v
		age = delta.days / 365
		if age > 120:
			raise ValidationError("MORE AGE!)")
		return v

person = Person(first_name="Alex", last_name="Li", birthday="1984-02-06")

print(str(person))
