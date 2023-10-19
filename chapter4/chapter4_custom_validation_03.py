from pydantic import field_validator, BaseModel

class Model(BaseModel):
	values: list[int]
	@field_validator("values", mode="before")
	def split_list(cls, v):
		if isinstance(v, str):	
			return v.split(",")
		return v

v = Model(values="1,2,3,4")
print(v.values)
