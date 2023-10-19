from pydantic import BaseModel, ValidationError, EmailStr, HttpUrl

class User(BaseModel):
	email: EmailStr
	website: HttpUrl

try:
	user = User(
		email="algaritmno822@gmail.com",
		website="http://localhost.com")
	print(user)
except ValidationError as e:
	print(str(e))
