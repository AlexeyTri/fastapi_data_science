from pydantic import BaseModel, EmailStr, ValidationError, model_validator

class Person(BaseModel):
	email: EmailStr
	password: str
	password_confirmation: str
	@model_validator(mode="after")
	def match_pass(self) -> 'Person':
		password = self.password
		password_confirmation = self.password_confirmation
		if password != password_confirmation: 	
			raise ValueErros("Password don't match")
		return self

person = Person(email="algarimtno822@gmail.com", password="111", password_confirmation="111")

print(str(person))
