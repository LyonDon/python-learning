#coding=utf-8
import unittest
from city_functions import city_country

class CityTestsCase(unittest.TestCase):
	"""测试city_functions.py"""
	def test_city_country(self):
		"""能否正确处理输入"""
		example=city_country("beijing",'china')
		pass

unittest.main()