"""
regex function, subset
char a - z
. 
*
"""

import unittest

class Test(unittest.TestCase):
	def test_regex_basic(self):
		self.assertEqual(regex('aa*', 'a'), True)
		self.assertEqual(regex('a.*', 'a'), True)
		self.assertEqual(regex('.', 'a'), True)
		self.assertEqual(regex('.*', 'anblskfj'), True)
		self.assertEqual(regex('a*', 'anblskfj'), False)
		self.assertEqual(regex('aaa', 'a'), False)
		self.assertEqual(regex('a*aa', 'aa'), True)
	def xtest_regex_edge(self):
		self.assertEqual(regex('a*', ''), True)
		self.assertEqual(regex('z*b*', ''), True)
		self.assertEqual(regex('.*j', 'anblskfj'), True)
		self.assertEqual(regex('.*k', 'anblskfj'), False)

def regex(pattern, string):
	pi = 0
	si = 0
	len_pattern = len(pattern) # do this so that we don't need to calculate length each time
	len_string = len(string)

	while pi < len_pattern and si < len_string:
		if pi + 1 < len_pattern and pattern[pi + 1] == '*':
			if pattern[pi] == '.':
				return True

			while si < len_string and pattern[pi] == string[si]:
				si += 1
			pi += 2

		elif pattern[pi] == '.':
			pi += 1
			si += 1

		elif ord('a') <= ord(pattern[pi]) <= ord('z'):
			if pattern[pi] == string[si]:
				pi += 1
				si += 1
			else:
				return False

	# at this point, check if we are in a valid state
	# if we haven't consumed all of the input s, we know it's invalid

	if si < len_string:
		return False

	# a* and '' are valid, in this case exit while loop for s
	# aaaaa and a are not valid, again, exited while loop for s
	while pi < len_pattern:
		if pi + 1 < len_pattern and pattern[pi + 1] == '*': # this is valid
			pi += 2
			# assume not multiple repeat in pattern. ex. a**
		else: # not _* 
			return False

	return True


def main():
	unittest.main()

if __name__ == "__main__":
	main()

