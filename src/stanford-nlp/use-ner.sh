#!/bin/sh

# use the model with 3 classes: classifiers/english.all.3class.distsim.crf.ser.gz
# however, if use conll data (4 classes), model changes to english.conll.4class.distsim.crf.ser.gz
./ner.sh sample.txt 
