import sys
from gensim.models import doc2vec

# get from https://radimrehurek.com/gensim/models/doc2vec.html
def processSentences(fname):
    sentences=doc2vec.TaggedLineDocument(fname)
    #print sentences
    model = doc2vec.Doc2Vec(sentences, size=100, window=8, min_count=1, workers=4)
    model.save('/tmp/my_model.doc2vec')

if __name__=="__main__":
    fname = sys.argv[1]
    processSentences(fname)
