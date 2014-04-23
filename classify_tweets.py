import classifier
import re

def getwords(document):
    splitter = re.compile('\\W*')
    words = [s.lower() for s in splitter.split(document) if len(s) > 3 and len(s) < 20]
    return dict([(w,1) for w in words])

cl = classifier.naivebayes(getwords)

# import tweets
tweets_file = open('tweets.tsv', 'r')

# count lines
line_count = 1
for line in tweets_file:
    line_count += 1

tweets_file.seek(0)

train_range =range(int(0.5 * line_count))
test_range = range(train_range[-1]+1, line_count)

# train classifier
for l in train_range:
    data = tweets_file.readline().split('\t')
    try:
        tweet_text = data[-1]
        party = data[2]
        cl.train(tweet_text, party)
    except:
        continue

# classify remaining data
correct = 0
unknown = 0
for m in test_range:
    data = tweets_file.readline().split('\t')
    try:
        tweet_text = data[-1]
        party = data[2]
        guess = cl.classify(tweet_text, default='unknown')
        if guess == party: correct += 1
        elif guess == 'unknown': unknown += 1
    except:
        continue

tweets_file.close()

precision = float(correct)/len(test_range)

# find combinations of features and categories
# so that we can see which words belong to D or R
word_combinations = cl.fcombi

# top words in classifier

items = ((word, party, value) for word in word_combinations for party, value in word_combinations[word].items())
ordered = sorted(items, key=lambda x: x[-1], reverse=True)

democrats = {}
republicans={}
for word, party, value in ordered:
    if party == 'D':
        democrats[word] = value
    elif party == 'R':
        republicans[word] = value

democrats_top25 = sorted(democrats.items(), key=lambda x: x[1], reverse=True)[:50]
republicans_top25 = sorted(republicans.items(), key=lambda x: x[1], reverse=True)[:50]