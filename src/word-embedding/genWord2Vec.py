import sys
from gensim.models import word2vec

# get from https://radimrehurek.com/gensim/models/word2vec.html
def processSentences(fname):
    sentences=word2vec.LineSentence(fname)
    #print sentences
    # if < min_count, no embedding
    model = word2vec.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
    model.save('/tmp/my_model.word2vec')

if __name__=="__main__":
    fname = sys.argv[1]
    processSentences(fname)

