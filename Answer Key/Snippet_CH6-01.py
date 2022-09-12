class Length:
	def __init__(self, inches):
		self._inches = inches

	@property
	def inches(self):
		return self._inches

	@inches.setter
	def inches(self, value):
		self._inches = value

	@property
	def centimeters(self):
		return self._inches * 2.54

	@centimeters.setter
	def centimeters(self, value):
		self._inches = value / 2.54

l = Length(1)
print("1 inch is " + str(l.centimeters) + " centimeters.")
l.centimeters = 5
print(str(l.centimeters) + " centimeters is " + str(l.inches) + " inches.")
