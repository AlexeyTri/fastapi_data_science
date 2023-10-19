from datetime import date
from pydantic import BaseModel, ValidationError
from enum import Enum

class Gender(str, Enum):
	MALE = "MALE"
	FEMALE = "FEMALE"
	NON_BINARY = "NON_BINARY"


class Address(BaseModel):
	street_address: str
	postal_address: str
	city: str
	country: str

class Person(BaseModel):
	first_name: str
	last_name: str
	birthday: date
	gender: Gender
	interesting: list[str]
	address: Address


try:
	person = Person(
		first_name = "ALex",
		last_name = "Litovchenko",
		birthday = "1984-02-06",
		gender = Gender.MALE,
		interesting = ["sport", "sport2"], address={
			"street_address": "Rimsky", "postal_address":  "123", "city" : "Moscow", "country" : "RF"})
	print (person)
except ValidationError as e:
	print(str(e))

