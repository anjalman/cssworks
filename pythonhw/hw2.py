

# word1="abc"
# word2="pqr"
# merg_word=""
# for i in range(0,3):    
#      merg_word+=word1[i]+word2[i]
# print(merg_word)



word1="ab"

word2="pqrs"  

result=""

smallest= word1  if  len(word1) < len(word2)  else  word2

largest= word1  if  len(word1) > len(word2)  else  word2

for i in range(0,len(smallest)):
         
         result+=word1[i]+word2[i]

bal_word= largest[len(smallest):]

result+=bal_word

print(result)