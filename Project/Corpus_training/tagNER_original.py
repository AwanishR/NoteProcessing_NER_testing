habitnerfile='NER_Files/habit.ner'
diagnerfile='NER_Files/diagnosis.ner'
procnerfile='NER_Files/procedure.ner'
drugnerfile='NER_Files/drug.ner'
def tagmedterm(text):
    fhabit=open(habitnerfile,'r')
    fdiag=open(diagnerfile,'r')
    fproc=open(procnerfile,'r')
    fdrug=open(drugnerfile,'r') 
    match = "no match xx"
    #print text
    for line in fhabit:
        #print line
        #print "in habit"
        if text.lower() == line.rstrip().lower():
            match = fhabit.name[fhabit.name.find("/")+1:fhabit.name.find(".")]
            break
    for line1 in fdiag:
        #print line1
        #print "in diag"
        if text.lower() == line1.rstrip().lower():
            match = fdiag.name[fdiag.name.find("/")+1:fdiag.name.find(".")]
            break
    for line2 in fproc:
        #print line2
        #print "in proc"
        if text.lower() == line2.rstrip().lower():
            match = fproc.name[fproc.name.find("/")+1:fproc.name.find(".")]
            break
    for line3 in fdrug:
        #print line3
        #print "in drug"
        if text.lower() == line3.rstrip().lower():
            match = fdrug.name[fdrug.name.find("/")+1:fdrug.name.find(".")]
            break
    fhabit.close()
    fdiag.close()
    fproc.close()
    fdrug.close()
    return match

def main():
    print "smoking is a " + tagmedterm("smoking")
    print "diabetes is a " + tagmedterm ("diabetes")
    print "mammo is a "+ tagmedterm ("mammo")
    print "SMoking is a " + tagmedterm("SMoking")
    print "letters is a " + tagmedterm("letters")
    print "in main"
if __name__=="__main__":
    main()
