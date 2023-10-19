from datetime import date
from pydantic import BaseModel,Field, ValidationError
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
	first_name: str = Field(..., min_length=3)
	last_name: str = Field(..., min_length=3)
	birthday: date
	age: int | None = Field(..., ge=0, le=120)
	gender: Gender
	interesting: list[str]
	address: Address


try:
	person = Person(
		first_name = "ALex",
		last_name = "Litovchenko",
		birthday = "1984-02-06",
		age = 39,
		gender = Gender.MALE,
		interesting = ["sport", "sport2"], address={
			"street_address": "Rimsky", "postal_address":  "123", "city" : "Moscow", "country" : "RF"})
	#return{person}
except ValidationError as e:
	print(str(e))

person_nested_include = person.model_dump(include = {
				"first_name": ...,
				"last_name": ...,
				"address":{"street_address", "counrty"},})

print(person_nested_include)

