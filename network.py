
import networkx as nx
import json
import pylab as plt

parties = ['D','R']

g = nx.DiGraph()


class xdict(dict):
	def add(self,e):
		if e in self:
			self[e] += 1
		else:
			self[e] = 1


for line in file('tweets.tsv'):
	parts = line.split("\t")
	name = parts[0]
	party = parts[2]
	g.add_node(name, group=parties.index(party))
	mentioned_sites = parts[5].split(",")
	for site in mentioned_sites:
		g.add_node(site,group=3)
		if name in g and site in g[name]:
			g[name][site]['weight'] += 1
		else:
			g.add_edge(name,site,weight=1)

# remove node with low degree
degrees = g.degree()
g.remove_node("")
for node in degrees:
	if degrees[node] < 10:
		g.remove_node(node)


# ordered list of node names
node_names = sorted(g.nodes())

# create links list
links = []
for e in g.edges():
	a,b = e
	value = g[a][b]['weight']
	links.append({'source':node_names.index(a),'target':node_names.index(b),'value': value})


nodes = g.nodes(data=True)

# create nodes list
node_list = [{'name':n[0],'group':n[1]['group']} for n in nodes]

# output json representation compatible with d3.js force-directed graph
print json.dumps({'links':links,'nodes':node_list},indent=4,sort_keys=True)

