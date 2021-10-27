import logging
import sys
import pytest

class BaseFramework:


	def setup(self):
		self.log = logging.getLogger(__class__.__name__)
		self.log.setLevel(logging.DEBUG)
		self.log.addHandler(logging.FileHandler("framework.log"))
		self.log.addHandler(logging.StreamHandler(sys.stdout))


