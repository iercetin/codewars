class Test:
	def assert_equals(a,b):
		print("Test - assert_equals \n:{}\n:{}".format(a,b))
		if a == b:
			print("*Success")
			return True
		print("*Failed")
		return False