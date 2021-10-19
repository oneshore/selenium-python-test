from animal import Animal

class Cat(Animal):
	sound = "Meow!"

	def __init__(self):
		super().__init__(Cat.sound)
