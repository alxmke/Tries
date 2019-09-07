from collections import defaultdict
class Trie:
	# takes a list of strings, words
	def __init__(self, words=[]):
		def _trie():
			return defaultdict(_trie)
		T = _trie()
		# put a stop condition for the empty Trie
		T[None]
		self.T = T

		# i have a couple ideas for a potentially more efficient first loading method
		for word in words:
			self.insert(word)

	# insert a word into the Trie
	def insert(self, word):
		T = self.T
		for c in word:
			T = T[c]
		T[None]

	# search for a match in the Trie, if not found, return a similar word
	def search(self, word):
		T = self.T
		nearest = ""
		found = True
		# use next(iter(dict)) to get a key out of the dict when there's no match
		for c in word:
			if c in T:
				T = T[c]
				nearest += c
			else:
				found = False
				break
		while(None not in T):
			found = False
			c = str(next(iter(T)))
			T = T[c]
			nearest += c
		return ("".join(nearest), found)
				
	#
	def autocompletions(self, word):
		def autocomplete(T,prefix):
			if not prefix:
				return [""]
			findings = []
			for k in T:
				endings = autocomplete(T[k],k)
				for ending in endings:
					findings.append(prefix+ending)
			return findings
		T = self.T
		for c in word:
			if c in T:
				T = T[c]
			else:
				return []
		return autocomplete(T,word)

	# TODO: make a helpful representation of Trie
	def __repr__(self):
		return self.T

	def __str__(self):
		return str(self.T)
# tests
if __name__ == '__main__':
	T = Trie(['bat', 'cat', 'car','catch','cash','cast','ca', 'capricorn'])
	S = Trie()
	tests = [
		(('car', True), T.search('car')),
		(('bat', False), T.search('bar')),
		(('', False), S.search('car')),
		(set(['cat', 'catch', 'car', 'cash', 'cast', 'ca', 'capricorn']), set(T.autocompletions('ca'))),
		([], T.autocompletions('X')),
		([], S.autocompletions('ca')),
	]
	failed = 0
	for i,test in enumerate(tests):
		try:
			assert test[0] == test[1]
		except:
			print(f"Failed test {i} where {test[0]} != {test[1]}")
			failed+=1
	if failed:
		print(f"Failed {failed} test(s) of {len(tests)} run.")
	else:
		print(f"Passed all tests of {len(tests)} run.")
