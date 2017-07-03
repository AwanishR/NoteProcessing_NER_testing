import datetime
#from datetime import datetime
import MySQLdb
#from time import gmtime, strftime
habitnerfile='NER_Files/habit.ner'
diagnerfile='NER_Files/diagnosis.ner'
procnerfile='NER_Files/procedure.ner'
drugnerfile='NER_Files/drug.ner'
vitalnerfile = 'NER_Files/vital.ner'
nounInFile = '../testing/output/set1/noun.txt'
finalOutputFile = 'NER_Output/set1/finalout.tx'
totalMatch =0
def tagmedterm(text):
    fhabit=open(habitnerfile,'r')
    fdiag=open(diagnerfile,'r')
    fproc=open(procnerfile,'r')
    fdrug=open(drugnerfile,'r')
    fvital=open(vitalnerfile,'r')
    global totalMatch
    match = "no match xx"
    #print text
    for line in fhabit:
        #print line
        #print "in habit"
        if text.lower() == line.rstrip().lower():
            match = fhabit.name[fhabit.name.find("/")+1:fhabit.name.find(".")] 
            totalMatch = totalMatch+1
            break
    for line1 in fdiag:
        #print line1
        #print "in diag"
        if text.lower() == line1.rstrip().lower():
            match = fdiag.name[fdiag.name.find("/")+1:fdiag.name.find(".")]
            totalMatch = totalMatch+1
            break
    for line2 in fproc:
        #print line2
        #print "in proc"
        if text.lower() == line2.rstrip().lower():
            match = fproc.name[fproc.name.find("/")+1:fproc.name.find(".")]
            totalMatch = totalMatch+1
            break
    for line3 in fdrug:
        #print line3
        #print "in drug"
        if text.lower() == line3.rstrip().lower():
            match = fdrug.name[fdrug.name.find("/")+1:fdrug.name.find(".")]
            break
    for line3 in fvital:
        #print line3
        #print "in drug"
        if text.lower() == line3.rstrip().lower():
            match = fvital.name[fvital.name.find("/")+1:fvital.name.find(".")]
            totalMatch = totalMatch+1
            break
    fhabit.close()
    fdiag.close()
    fproc.close()
    fdrug.close()
    fvital.close()
    return match

def main():
    db = MySQLdb.connect(host ="localhost", user ="root", passwd = "root", db = "nlp")
    cur = db.cursor()
    startTime = datetime.datetime.now()
    print "Processing NER matcher ..."
    nounFile = open(nounInFile,'r')
    ffinal = open (finalOutputFile,'w')
    noteId = "0"
    setId = "set1"
    cur.execute("delete from ner where set_id = %s",(setId))
    for line in nounFile:
        words = line.split()
        for word in words:
            if "Note_Number" not in word:
                #print "Detected Noun::"+word
                #print word+" is "+ tagmedterm(word)
                matchedValue = tagmedterm(word)
                ffinal.write("Detected Noun::"+word+"\n")
                ffinal.write(word+" is "+ matchedValue+"\n")
                cur.execute("insert into ner (note_id,detected_element,element_type,set_id,updated_date) values(%s,%s,%s,%s,%s)",
                            (noteId,word,matchedValue,setId,str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
            else:
                ffinal.write("\n"+word)
                noteId=word
    print "in main"
    nounFile.close()
    print "NER matcher completed..."
    endTime = datetime.datetime.now()
    timeDiff =endTime-startTime
    formattedTime = divmod (timeDiff.days*86400+timeDiff.seconds,60)
    print "Total Time taken is " + str(formattedTime[0])+" munutes and "+str(formattedTime[1])+" seconds"
    print "Total match found::"+str(totalMatch)
if __name__=="__main__":
    main()
