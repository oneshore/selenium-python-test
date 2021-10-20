class Animal:
	total = 0

	def __init__(self, sound):
		self._sound = sound


	def speak(self, word=""):
		print(self._sound, word)

	def _move(self, distance=1):
		print(f"{self.__class__.__name__} moves {distance}")

	def walk(self, distance=1):
		self._move(distance)

	def run(self, distance=1):
		self._move(distance*2)
