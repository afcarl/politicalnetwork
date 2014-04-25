
import networkx as nx

g = nx.DiGraph()


class xdict(dict):
	def add(self,e):
		if e in self:
			self[e] += 1
		else:
			self[e] = 1


names = xdict()
sites = xdict()

for line in file('tweets.tsv'):
	parts = line.split("\t")
	name = parts[0]
	mentioned_sites = parts[5].split(",")
	for site in mentioned_sites:
		if name in g and site in g[name]:
			g[name][site]['weight'] += 1
		else:
			g.add_edge(name,site,weight=1)

for e in g.edges():
	a,b = e
	print e, g[a][b]
		

nx.write_graphml(g,"sites.graphml")








