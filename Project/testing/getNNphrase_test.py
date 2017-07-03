import nltk
from nltk import word_tokenize
from nltk import pos_tag
import re

#Open sentence detector model
sentence_detector = nltk.data.load("tokenizers/punkt/english.pickle")
#Open notes file for reading
#noteFile = open ('testing/test_data/test_data.txt','r')
#Opens output file for writing
#fileToWrite = open("testing/output/processednotes.txt","w")
#Opens tree bank file for writing
#fileTreeBank  = open ("testing/output/treeBank.txt","w+")
#print "Processing note of file "+noteFile.name+"...."
#noteCount = 1
tokenCount =0
sentCount=0
'''for line in noteFile:
    print "Note Number ---->"+ str(noteCount)
    print "Original note Text read from file\n"+line
    #Sentence Detection
    sentences = sentence_detector.tokenize(line.strip())
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
        #Write tokens into file
        for item in tokens:
            fileToWrite.write("\n----\n{}".format(item))
            tokenCount+=len(item)
        fileToWrite.write("\n*****POS Tagging [using Penn Treebank tagging]****\n")
        #Write POS tag in file
        for item in postag:
            fileToWrite.write("{} ".format(item))
            fileTreeBank.write("{}".format(item))
        fileToWrite.write("\n")
        fileTreeBank.write("\n")
        #Write in tree  bank
        ##for index in range (len(postag)):
            ##fileTreeBank.write("\n"+str(postag[index]))
            #print ("\n"+str(postag[index]))
    sentCount+=len(sentences)
    noteCount = noteCount+1'''
fileTreeBankRead  = open ("testing/output/treeBank1.txt","r")
nounOutFile = open ("testing/output/noun.txt","w")
noteNum = 1
#print("new file -----------",fileTreeBankRead.name)
for line in fileTreeBankRead:
     print ("line****",line)
     #print ("line-rev",line[::-1])
     rline = line[::-1]
     nounOutFile.write("Note Number-"+ str(noteNum)+":")
     for m in re.finditer("NN",rline):
        #print m
        l1=rline[m.start()+2:len(line)]
        #print "find ---->>" + m.rfind(',',0)
        #print (l1)
        l2=l1[l1.find(",'")+2:l1.find("'(")]
        #print (l2)
        print ("Noun detected "+l2[::-1])
        nounOutFile.write(l2[::-1]+"\t")
        #diag=l2.lstrip()
        #print habit
        #diagCorpus = open (diagfilename,'a')
        #diagCorpus.write(diag.strip().lower()+"\n")                        
        #diagCorpus.close()
     nounOutFile.write ("\n")   
     noteNum=noteNum+1
fileTreeBankRead.close()
nounOutFile.close()
#fileToWrite.close()
#fileTreeBank.close()
#Dsiplays
print ("\nTotal number of sentences detected :",sentCount)
print("\nTotal number of tokens detected :",tokenCount)
#noteFile.close()
print ("\nProcessing completed!!!")


                
