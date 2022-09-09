class World:
	def __init__(self):
		print("I'm alive!")
	def __del__(self):
		print("I'm gone!")

earth = World()
del(earth)
