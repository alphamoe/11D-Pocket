#!/bin/sh

# may need to have slf4j at first: https://www.slf4j.org/download.html
# austen.prop -- a properties file
java -cp "stanford-ner.jar:slf4j-api-1.7.22.jar" edu.stanford.nlp.ie.crf.CRFClassifier -prop austen.prop

# test the model if needed
# ner-model.ser.gz -- a model file
java -cp "stanford-ner.jar:slf4j-api-1.7.22.jar:slf4j-simple-1.7.22.jar" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile jane-austen-emma-ch2.tsv
