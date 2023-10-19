from pydantic import Field, BaseModel, ValidationError
from datetime import datetime

def list_factory():
	return ["a", "b", "c"]

class Model(BaseModel):
	l: list[str] = Field(default_factory=list_factory)
	d: datetime = Field(default_factory=datetime.now)
	l2: list[str] = Field(default_factory=list)

try:
	model = Model(l=["a"], l2=["b"])
	print(model)
except ValidationError as e:
	print(str(e))


