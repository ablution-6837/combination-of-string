from itertools import permutations
def allPermutations(str):
       
     
     permList = permutations(str)
  
     
     for perm in list(permList):
         print (''.join(perm))
        

name=['A','P','P','L','E']
comb=[]
l=len(name)
for i in range(0,l):
     stri=name[i]
     comb.insert(i,stri)
     if __name__ == "__main__":
      str =comb
      allPermutations(str)
     
     
     