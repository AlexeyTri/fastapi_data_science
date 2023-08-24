class Temperature:
	def __init__(self, value, scale):
		self.value = value
		self.scale = scale
	def __repr__(self):
		return f"Temperature {self.value}, {self.scale!r}"
	def __str__(self):
		return f"Temperature is {self.value} O{self.scale}"
c = Temperature(25, "C")
print(repr(c))
print(str(c))
