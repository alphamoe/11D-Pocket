import json
import sys

def process(fname):
    data={}
    with open(fname) as f:
        for line in f:
            content = json.loads(line)
            #print content
            if 'docs' in content:
                for doc in content['docs']:
                    if 'text' in doc:
                        #print doc
                        #print doc['text'], doc['match']
                        if doc['match'] not in data:
                            data[doc['match']] = [doc['text']]
                        else:
                            data[doc['match']].append(doc['text'])
    return data

def save2md(data):
    f = open('reading.notes.md', 'w')
    for key, value in data.iteritems():
        #print key, value
        title = "["+key+"]("+key+")"
        f.write(title+"\n")
        for doc in value:
            f.write("```\n")
            f.write(doc+"\n")
            f.write("```\n")
    f.close()

if __name__=="__main__":
    fname = sys.argv[1]
    data = process(fname)
    save2md(data)