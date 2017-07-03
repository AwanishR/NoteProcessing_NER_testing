import nltk
from nltk import word_tokenize
from nltk import pos_tag

#Open sentence detector model
sentence_detector = nltk.data.load("tokenizers/punkt/english.pickle")
#Open notes file for reading
fileName ="f:/NLP/data/forTest.txt"
noteFile = open (fileName,"r+")
#Opens output file for writing
fileToWrite = open("processednotes.txt","w")
#Opens tree bank file for writing
fileTreeBank  = open ("treeBank.txt","w+")
fileNER=open("ner.txt","w+")
print ("Processing note of file ",noteFile.name,"....")
tokenCount =0
sentCount=0
grammar ="NP : {<DT>?<JJ>*<NN>}"
chunkParser = nltk.RegexpParser(grammar)
for line in noteFile:
    print("Original note Text read from file\n",line)
    #Sentence Detection
    sentences = sentence_detector.tokenize(line.strip())
    print (sentences)
    for index in range (len(sentences)):
        #Preprocessing dictionary
        abbr ={' pt ':' patient ','Pt':'Patient',' dx ':' diagnosis ',' hx ':' history ','f/u':'follwup','n\'t':' not','appt':'appointment','meds':'medication','yrs':'years','wt':'weight','hsp':'hospital','malfx':'malfunction','unsat':'unsaturated','F/u':'Follow up','carbs':'carbohydrade'}
        processedSentence = sentences[index]
        #Preprocessing
        for k,v in abbr.items():
            processedSentence=processedSentence.replace(k,v)
            #print (k,v)
        #print ("Original Sentence:++++"+sentences[index])
        #print ("\nPreprocessed Sentence:---->"+processedSentence)
        fileToWrite.write("\nOriginal Sentence"+str(index+1)+" >>> "+sentences[index])
        fileToWrite.write("\nPreprocessed Sentence:>>>:"+processedSentence+" <<<\n\nTokens of this sentence are as follows\n")
        #fileTreeBank.write("\nOriginal Sentence"+str(index+1)+" >>> "+sentences[index])
        #fileTreeBank.write("\nPreprocessed Sentence:>>>:"+processedSentence+" <<<\n----POS Tagging---\n")
        #Tokenization
        tokens = word_tokenize(processedSentence)
        #POS Tagging [PennTreebank tagger]
        postag=pos_tag(tokens);
        print (nltk.ne_chunk(postag))
        #fileNER.write(nltk.ne_chunk(postag))
        #fileNER.close()
        #Write tokens into file
        for item in tokens:
            fileToWrite.write("\n----\n{}".format(item))
            tokenCount+=len(item)
        fileToWrite.write("\n*****POS Tagging [using Penn Treebank tagging]****\n")
        #Write POS tag in file
        print (postag)
        tree = chunkParser.parse(postag)
        
        #print (tree.leaves())
        fileTreeBank.write(tree.pformat(parens="[]"))
        for item in postag:
            fileToWrite.write("{} ".format(item))
            #tree = chunkParser.parse(item)
            #fileTreeBank.write("{}".format(item))            
        fileToWrite.write("\n")
        fileTreeBank.write("\n")
        #Write in tree  bank
        ##for index in range (len(postag)):
            ##fileTreeBank.write("\n"+str(postag[index]))
            #print ("\n"+str(postag[index]))
    sentCount+=len(sentences)
fileTreeBankRead  = open ("treeBank.txt","r")
print("new file -----------",fileTreeBankRead.name)
for lines in fileTreeBankRead:
     print ("line****",lines)
fileTreeBankRead.close()
fileToWrite.close()
fileTreeBank.close()
#Dsiplays
print ("\nTotal number of sentences detected :",sentCount)
print("\nTotal number of tokens detected :",tokenCount)
noteFiles = open (fileName,"r")
countFiles = open ("wordcount.txt","w+")
from collections import Counter
wordcount = Counter(noteFiles.read().split())
for item in wordcount.items():
    print("{}\t{}".format(*item))
    countFiles.write("{}\t{}\n".format(*item))
print (wordcount)
#countFiles.write(wordcount)
countFiles.close()
noteFiles.close()
noteFile.close()
print ("\nProcessing completed!!!")
