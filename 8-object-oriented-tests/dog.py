from animal import Animal

class Dog(Animal):
	sound = "Woof!"

	def __init__(self):
		super().__init__(Dog.sound)
