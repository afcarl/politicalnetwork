
import re

labMT_scores = {}
for line in file('labMT.tsv'):
	parts = line.split('\t')
	word = parts[0]
	score = float(parts[2])
	labMT_scores[word] = score

def calculate_score(text):
	tokens = text.split()
	labmt_words = []
	for token in tokens:
		token = re.sub(r'\W+', '', token)
		if token in labMT_scores:
			labmt_words.append(token)
	return sum([labMT_scores[word] for word in labmt_words]) / float(len(labmt_words))
		










