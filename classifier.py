import re

def getwords(document):
    splitter = re.compile('\\W*')

    words = [s.lower() for s in splitter.split(document) if len(s) > 3 and len(s) < 20 ]

    return dict([(w,1) for w in words])


class classifier(object):
    def __init__(self, getfeatures, filename=None):
        # count of feature combinations
        self.fcombi = {}
        # count of documents in each category
        self.ccount = {}
        self.getfeatures = getfeatures

    # Increase the count of a feature/category pair
    def incf(self,f,cat):
         self.fcombi.setdefault(f,{})
         self.fcombi[f].setdefault(cat,0)
         self.fcombi[f][cat]+=1


     # Increase the count of a category
    def incc(self,cat):
         self.ccount.setdefault(cat,0)
         self.ccount[cat]+=1


     # The number of times a feature has appeared in a category
    def fcount(self,f,cat):
         if f in self.fcombi and cat in self.fcombi[f]:
             return float(self.fcombi[f][cat])
         return 0.0

     # The number of items in a category
    def catcount(self,cat):
         if cat in self.ccount:
             return float(self.ccount[cat])
         return 0

     # The total number of items
    def totalcount(self):
         return sum(self.ccount.values( ))

     # The list of all categories
    def categories(self):
         return self.ccount.keys( )

    def train(self,item,cat):
        features = self.getfeatures(item)
        for f in features:
            self.incf(f,cat)

        self.incc(cat)

    def fprob(self,f,cat):
        if(self.catcount(cat) == 0): return 0
        return self.fcount(f,cat)/self.catcount(cat)

    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        # Calculate current probability
        basicprob=prf(f,cat)
        # Count the number of times this feature has appeared in
        # all categories
        totals=sum([self.fcount(f,c) for c in self.categories( )])
        # Calculate the weighted average
        bp=((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp


class naivebayes(classifier):
    def __init__(self,getfeatures):
        classifier.__init__(self,getfeatures)
        self.thresholds={}

    def docprob(self,item,cat):
        features=self.getfeatures(item)
        # Multiply the probabilities of all the features together
        p=1
        for f in features: p*=self.weightedprob(f,cat,self.fprob)
        return p

    def prob(self,item,cat):
        catprob=self.catcount(cat)/self.totalcount( )
        docprob=self.docprob(item,cat)
        return docprob*catprob

    def setthreshold(self,cat,t):
        self.thresholds[cat]=t

    def getthreshold(self,cat):
        if cat not in self.thresholds: return 1.0
        return self.thresholds[cat]

    def classify(self,item,default=None):
        probs={}
        # Find the category with the highest probability
        max=0.0
        for cat in self.categories( ):
            probs[cat]=self.prob(item,cat)
            if probs[cat]>max:
                max=probs[cat]
                best=cat

        # Make sure the probability exceeds threshold*next best
        for cat in probs:
            if cat==best: continue
            if probs[cat]*self.getthreshold(best)>probs[best]: return default
        return best
