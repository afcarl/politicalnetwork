import classifier
import re

def getwords(document):
    splitter = re.compile('\\W*')

    words = [s.lower() for s in splitter.split(document) if len(s) > 3 and len(s) < 20 ]

    return dict([(w,1) for w in words])

cl = classifier(getwords)