import sys

def insertioncount(s,l,h):
    if(l>h):
        return "INFINITE"
    elif(l==h):
        return int(0)
    elif(l==(h-1)):
        if(s[l]==s[h]):
            return 0
        else:
            return 1
    
    else:
        if(s[l]==s[h]):
            return insertioncount(s,l+1,h-1)
        else:
            #c=insertioncount(s,l,h-1)
            #d=insertioncount(s,l+1,h)
            return((min(insertioncount(s,l,h-1),insertioncount(s,l+1,h))) + 1)
            #n=m+1
            #return n




a=insertioncount("abcdb",0,2)

    
print a
#print b
#print c
#print d
#print e

    
