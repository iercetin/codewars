class Test:
	def assert_equals(a,b,whatever="fuckit"):
		print("Test - assert_equals \nGiven    : {}\nCorrect  : {}".format(a,b))
		if a == b:
			print("*Success")
			return True
		print("*Failed")
		return False