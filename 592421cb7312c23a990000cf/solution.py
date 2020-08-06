# Look and say sequence generator
# https://www.codewars.com/kata/592421cb7312c23a990000cf


def next_number(s):
	result = []
	s = list(str(s))
	i = 0
	if len(s) == 1:
		result = [1,int(s[0])]

	count = 1
	for i in range(1,len(s)):
		el = s[i]
		bef = s[i-1]

		if el == bef:		
			count += 1
			if i == len(s) - 1:
				result.append(count)
				result.append(bef)

		else:
			result.append(count)
			result.append(bef)
			count = 1

			if i == len(s) - 1:
				result.append(count)
				result.append(el)

	return "".join([str(e) for e in result])

def look_and_say_sequence(first_element, n):
    r = first_element
    while n > 1:
    	r = next_number(r)
    	n -= 1
    return r