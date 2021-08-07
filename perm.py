from itertools import permutations

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def allPermutations(str):
       
     
     permList = permutations(str)
  
     
     for perm in list(permList):
         print (''.join(perm))
        

name=input("Enter The String\n")
Convert(name)
comb=[]
l=len(name)
for i in range(0,l):
     stri=name[i]
     comb.insert(i,stri)
     str =comb
     allPermutations(str)
     
     
     
     
     
