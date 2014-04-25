
import networkx as nx

class xdict(dict):
	def add(self,e):
		if e in self:
			self[e] += 1
		else:
			self[e] = 1


names = xdict()
freqs = xdict()

for line in file('tweets.tsv'):
	parts = line.split("\t")
	freqs.add( len(parts) )
		
print freqs









