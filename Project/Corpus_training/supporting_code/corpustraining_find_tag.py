import re
import datetime
trainfilename ='../training_data/en-ner-medical.txt'
habitfilename='habittemp1.ner'
habitfilenamenodups='habit1.ner'
procfilename='proceduretemp1.ner'
procfilenamenodups='procedure1.ner'
diagfilename='diagnosistemp1.ner'
diagfilenamenodups='diagnosis1.ner'
drugfilename='drugtemp1.ner'
drugfilenamenodups='drug1.ner'
vitalfilename='vitaltemp1.ner'
vitalfilenamenodups='vital1.ner'
alltagfilename='alltagtempwithtags1.ner'
alltagfilenamenodups='alltagwithtags1.ner'
fileToRead = open (trainfilename,'r')
habitCorpus = open (habitfilename,'w')
procCorpus = open (procfilename,'w')
diagCorpus = open (diagfilename,'w')
drugCorpus = open (drugfilename,'w')
vitalCorpus = open (vitalfilename,'w')
alltagCorpus = open (alltagfilename,'w')
notecount=0
print "Training Started ....."
startTime = datetime.datetime.now()
for line in fileToRead:
    c=line.count("<START:")
    d=line.count("<END>")
    #print "Total Start tag :"+str(c)
    #print "Total end tag:" + str(d)
    if c<>d:
        print line
        print "Total Start tag :"+str(c)
        print "Total end tag:" + str(d)
        
    
    '''#HABIT Corpus
    for m in re.finditer("<START:h",line):
        print ("Habit found",m.start())
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(":")+1:l1.find(">")]
        habit=l2.lstrip()
        #print habit
        habitCorpus = open (habitfilename,'a')
        habitCorpus.write(habit.strip().lower()+"\n")                        
        habitCorpus.close()'''
        
    #PROCEDURE Corpus
    '''for m in re.finditer("<START:proced",line):
        """print ("Habit found",m.start()) """
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(":")+1:l1.find(">")]
        proc=l2.lstrip()
        #print habit
        procCorpus = open (procfilename,'a')
        procCorpus.write(proc.strip().lower()+"\n")                        
        procCorpus.close() '''  
    #DIAG Corpus
    '''for m in re.finditer("<START:d",line):
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(":")+1:l1.find(">")]
        diag=l2.lstrip()
        #print habit
        diagCorpus = open (diagfilename,'a')
        diagCorpus.write(diag.strip().lower()+"\n")                        
        diagCorpus.close()
        
    #DRUG Corpus
    for m in re.finditer("<START:drug",line):
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(">")+1:l1.find("<")]
        drug=l2.lstrip()
        #print habit
        drugCorpus = open (drugfilename,'a')
        drugCorpus.write(drug.strip().lower()+"\n")                        
        drugCorpus.close(

    #VITAL Corpus
    for m in re.finditer("<START:v",line):
        l1=line[m.start()+1:len(line)]
        #print (l1)
        l2=l1[l1.find(":")+1:l1.find(">")]
        vital=l2.lstrip()
        #print habit
        vitalCorpus = open (vitalfilename,'a')
        vitalCorpus.write(vital.strip().lower()+"\n")                        
        vitalCorpus.close()'''
   
    '''  #Total tag Corpus
    for m in re.finditer("<END>",line):
        l1=line[m.start()-30+1:len(line)]
        #print (l1)
        l2=l1[:l1.find("<END>")]
        alltag=l2.lstrip()
        #print habit
        alltagCorpus = open (alltagfilename,'a')
        alltagCorpus.write(alltag.strip().lower()+"\n")                        
        alltagCorpus.close()'''
    #notecount=notecount+1
    
procCount=0
vitalCount = 0
diagCount = 0
habitCount =0
drugCount = 0
alltagCount=0
'''#--Remove dups from Procedure corpus
lines_seen = set() # holds lines already seen
outfile = open(procfilenamenodups, "w")
for line in open(procfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        procCount = procCount+1
outfile.write(">>Total Procedures detected << " + str (procCount))
outfile.close()'''
'''#--Remove dups from Habit corpus
lines_seen = set() # holds lines already seen
outfile = open(habitfilenamenodups, "w")
for line in open(habitfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        habitCount = habitCount+1
outfile.write(">>Total Habits detected << " + str (habitCount))
outfile.close()'''
'''#--Remove dups from Diagnosis corpus
lines_seen = set() # holds lines already seen
outfile = open(diagfilenamenodups, "w")
for line in open(diagfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        diagCount = diagCount+1
outfile.write(">>Total Diagnosis detected << " + str (diagCount))            
outfile.close()'''
'''#--Remove dups from drug corpus
lines_seen = set() # holds lines already seen
outfile = open(drugfilenamenodups, "w")
for line in open(drugfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        drugCount = drugCount+1
outfile.write(">>Total Drugs detected << " + str (drugCount))      
outfile.close()'''
'''#--Remove dups from vital corpus
lines_seen = set() # holds lines already seen
outfile = open(vitalfilenamenodups, "w")
for line in open(vitalfilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        vitalCount = vitalCount+1
outfile.write(">>Total Vitals detected << " + str (vitalCount)) 
outfile.close()'''

'''#--Remove dups from all tag corpus
lines_seen = set() # holds lines already seen
outfile = open(alltagfilenamenodups, "w")
readfile = open(alltagfilename, "r")
for line in readfile:
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
        alltagCount = alltagCount+1
outfile.write(">>Total tags detected << " + str (alltagCount)) 
outfile.close()
readfile.close()'''

print "Training Ended !!"
endTime = datetime.datetime.now ()
#print "Total Training notes->" + str (notecount)
timeDiff =endTime-startTime
#datetime.timedelta(0, 8, 562000)
formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
print "Total Time taken to train " + str(notecount)+" notes is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
#print ">>Total Procedure detected << " + str (procCount)
#print ">>Total Diagnosis detected << " + str (diagCount)
#print ">>Total Drugs detected << " + str (drugCount)
#print ">>Total Habits detected << " + str (habitCount)
#print ">>Total Vitals detected << " + str (vitalCount)
#print ">>Total tags detected << " + str (alltagCount)
